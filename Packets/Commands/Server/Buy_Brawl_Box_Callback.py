from Packets.Messages.Server.Out_Of_Sync_Message import OutOfSyncMessage
from random import *
from Database.DatabaseManager import DataBase
from Logic.Boxes import Boxes

from Utils.Writer import Writer


class ServerBox(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24111
        self.player = player
        self.BoxData = Boxes.boxes

    def encode(self):
        reward_list = ["Nothing", "Brawler", "Tickets", "Gems", "TokensDoubler"]
        unlocked_brawlers = []
        unlockable_brawlers = []

        for brawlers_id in self.player.BrawlersUnlockedState:
            if self.player.BrawlersUnlockedState[brawlers_id] == 0:
                unlockable_brawlers.append(int(brawlers_id))
            elif self.player.BrawlersUnlockedState[brawlers_id] == 1 and self.player.Brawler_level[brawlers_id] != 8:
                unlocked_brawlers.append(int(brawlers_id))

        self.box_index = 0
        def get_id(id):
            if id == 5:  # Brawl Box
                DataBase.replaceValue(self, 'brawlBoxes', self.player.brawl_boxes - 100)
                return 10
            elif id == 4:  # Big Box
                self.box_index = 1
                DataBase.replaceValue(self, 'bigBoxes', self.player.big_boxes - 10)
                return 12
            elif id == 3:  # Shop Mega Box
                self.box_index = 3
                DataBase.replaceValue(self, 'gems', self.player.gems - 80)
                return 11
            elif id == 1:  # Shop Big Box
                self.box_index = 2
                DataBase.replaceValue(self, 'gems', self.player.gems - 30)
                return 12

        self.box_skin_id = get_id(self.player.box_id)
        box_content = {"RewardType": "", "RewardCount": 1, "Gold": randint(self.BoxData[self.box_index]["Coins"][0], self.BoxData[self.box_index]["Coins"][1])}
        reward = choices(reward_list, weights=[0.5, 0.18, 0.15, 0.09, 0.05], k=1)

        if reward[0] == "Brawler" and len(unlockable_brawlers) == 0:
            reward_list.pop(1)
            reward = choices(reward_list, weights=[0.5, 0.15, 0.09, 0.05], k=1)

        brawlers_rewarded = []
        choosed_brawler = choice(unlocked_brawlers)

        # Brawler randomizer
        while len(brawlers_rewarded) != self.BoxData[self.box_index]["MaxUpgradePoints"]:
            if len(unlocked_brawlers) < self.BoxData[self.box_index]["MaxUpgradePoints"]:
                for i in range(len(unlocked_brawlers)):
                    brawlers_rewarded.append(unlocked_brawlers[i])
                break
            elif choosed_brawler not in brawlers_rewarded:
                brawlers_rewarded.append(choosed_brawler)
            else:
                choosed_brawler = choice(unlocked_brawlers)

        # Reward manager
        if reward[0] == "Brawler":
            box_content["RewardType"] = reward[0]
            if self.BoxData[self.box_index]["NewCharPosition"] == "Start":
                box_content["RewardCount"] = 1
            elif self.BoxData[self.box_index]["NewCharPosition"] == "Middle":
                brawlers_rewarded.pop(len(brawlers_rewarded) - 1)
                box_content["RewardCount"] = 2 + len(brawlers_rewarded)
                for i in range(len(brawlers_rewarded)):
                    box_content["Powerpoints" + str(i + 1)] = brawlers_rewarded[i]
            else:
                box_content["RewardCount"] = 2 + len(brawlers_rewarded)
                for i in range(len(brawlers_rewarded)):
                    box_content["Powerpoints" + str(i + 1)] = brawlers_rewarded[i]
            box_content["Brawler"] = choice(unlockable_brawlers)
            self.player.BrawlersUnlockedState[str(box_content["Brawler"])] = 1
            DataBase.replaceValue(self, 'UnlockedBrawlers', self.player.BrawlersUnlockedState)

        elif reward[0] == "Nothing":
            box_content["RewardType"] = "OnlyPowerpoints"
            for i in range(len(brawlers_rewarded)):
                box_content["RewardCount"] += 1
                box_content["Powerpoints" + str(i + 1)] = brawlers_rewarded[i]
        else:
            box_content["RewardType"] = "Bonus"
            for i in range(len(brawlers_rewarded)):
                box_content["RewardCount"] += 1
                box_content["Powerpoints" + str(i + 1)] = brawlers_rewarded[i]
            box_content["RewardCount"] += 1
            box_content[reward[0]] = self.BoxData[self.box_index][reward[0]]

        # Box info
        self.writeVint(203) # CommandID
        self.writeVint(0)   # Unknown
        self.writeVint(1)   # Unknown
        self.writeVint(self.box_skin_id)  # BoxID
        # Box info end

        # Reward start
        self.writeVint(box_content["RewardCount"]) # Reward count

        if box_content["RewardType"] == "Brawler" and self.BoxData[self.box_index]["NewCharPosition"] == "Start":
            # Brawler start
            self.writeVint(1)                           # Reward amount
            self.writeScId(16, box_content["Brawler"])  # CsvID
            self.writeVint(1)                           # RewardID
            self.writeHexa('''00 00 00''')              # Reward end
            # Brawler end

        else:
            DataBase.replaceValue(self, 'gold', self.player.gold + box_content["Gold"])
            # Gold start
            self.writeVint(box_content["Gold"]) # Reward amount
            self.writeScId(0, 7)                # RewardID
            self.writeHexa('''00 00 00''')  # Reward end
            # Gold end

            powerpoints_ammount = [randint(self.BoxData[self.box_index]["UpgradePoints"][0], self.BoxData[self.box_index]["UpgradePoints"][1]) for _ in range(len(brawlers_rewarded))]
            powerpoints_ammount.sort()
            for i in range(len(brawlers_rewarded)):
                self.player.brawlers_upgradium[str(brawlers_rewarded[i])] += powerpoints_ammount[i]
                DataBase.replaceValue(self, 'brawlersUpgradePoints', self.player.brawlers_upgradium)
                # Upgrade points start
                self.writeVint(powerpoints_ammount[i]) # Reward amount
                self.writeScId(16, box_content["Powerpoints" + str(i + 1)]) # BrawlerID
                self.writeVint(6) # RewardID
                self.writeHexa('''00 00 00''')  # Reward end
                # Upgrade points end

            if box_content["RewardType"] == "Brawler":
                if self.BoxData[self.box_index]["NewCharPosition"] == "End" or self.BoxData[self.box_index]["NewCharPosition"] == "Middle":
                    # Brawler start
                    self.writeVint(1)  # Reward amount
                    self.writeScId(16, box_content["Brawler"])  # CsvID
                    self.writeVint(1)  # RewardID
                    self.writeHexa('''00 00 00''')  # Reward end
                    # Brawler end

            if box_content["RewardType"] == "Bonus":
                for i in range(len(Boxes.reward_id)):
                    if Boxes.reward_id[i]["Name"] == reward[0]:
                        if reward[0] == "Gems":
                            ammountrewarded = choice(box_content[reward[0]])
                            self.player.gems = self.player.gems + ammountrewarded
                            DataBase.replaceValue(self, 'gems', self.player.gems)
                        elif reward[0] == "Tickets":
                            ammountrewarded = choice(box_content[reward[0]])
                            self.player.tickets = self.player.tickets + ammountrewarded
                            DataBase.replaceValue(self, 'tickets', self.player.tickets)
                        else:
                            ammountrewarded = choice(box_content[reward[0]])
                            self.player.tokensdoubler = self.player.tokensdoubler + ammountrewarded
                            DataBase.replaceValue(self, 'tokensdoubler', self.player.tokensdoubler)
                        self.writeVint(ammountrewarded) # Reward ammount
                        self.writeScId(0, Boxes.reward_id[i]['ID']) # RewardID
                        break

        # Box end
        for i in range(13):
            self.writeVint(0)