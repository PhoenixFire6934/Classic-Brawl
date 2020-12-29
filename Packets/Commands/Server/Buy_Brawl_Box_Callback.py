from Packets.Messages.Server.OutOfSyncMessage import OutOfSyncMessage
import json
from os import read
from Utils.Writer import Writer
import random
from Database.DataBase import DataBase
from Logic.Boxes import Boxes

class ServerBox(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24111
        self.player = player

    def encode(self):
        reward_list = [0, "Tickets", "TokensDoubler", "Gems"]
        
        unlocked_brawlers = []
        unlockable_brawlers = []
        for brawlers_id in self.player.BrawlersUnlockedState:
            if self.player.BrawlersUnlockedState[brawlers_id] == 0:
                unlockable_brawlers.append(int(brawlers_id))
            else:
                unlocked_brawlers.append(int(brawlers_id))

        if self.player.boxID == 5:
            OutOfSyncMessage(self.client, self.player, "Only big box work at the moment").send()

        if self.player.boxID == 4:
            reward = random.choices(reward_list, weights=[7, 0.8, 0.7, 1])
            BoxData = Boxes.boxes
            GoldValue = random.randrange(BoxData[1]['MinCoins'], BoxData[1]['MaxCoins'])
            BrawlersRewarded = random.sample(unlocked_brawlers, k=len(unlocked_brawlers))

            if reward[0] == 0 and len(unlocked_brawlers) >= 3:
                totalreward = 4

            elif reward[0] == 0 and len(unlocked_brawlers) < 3:
                totalreward = 2 + len(unlocked_brawlers)

            else:
                totalreward = 5

            if reward == 8:
                newGems = self.player.gems + 100
                DataBase.replaceValue(self, 'gems', newGems)
            elif reward == 3:
                newTickets = self.player.tickets + 100
                DataBase.replaceValue(self, 'tickets', newTickets)
            elif reward == 2:
                value = 100

            newBigBox = self.player.bigBoxes - 10
            DataBase.replaceValue(self, 'bigBoxes', newBigBox)

            self.writeVint(203)
            self.writeVint(0)
            self.writeVint(1)
            self.writeVint(12)
            self.writeVint(totalreward)
            
            self.writeVint(GoldValue)
            self.writeVint(0)
            self.writeVint(7)
            self.writeVint(0)

            self.writeVint(0)
            self.writeVint(0) # Reward end

            for i in range(1, totalreward):
                print(i)
                if i == 4:
                    break
                elif i == totalreward - 1 and len(unlockable_brawlers) > 0:
                    for unlocked_brawlers in self.player.BrawlersUnlockedState:
                        if self.player.BrawlersUnlockedState[unlocked_brawlers] == 0:
                            
                            self.writeVint(1) # Reward ammount
                            self.writeVint(16) # Csv id
                            self.writeVint(int(unlocked_brawlers)) # Brawler id
                            self.writeVint(1) # Reward id

                            self.writeVint(0)
                            self.writeVint(0) # Reward end
                            self.writeVint(0)
                            self.player.BrawlersUnlockedState[unlocked_brawlers] = 1

                            DataBase.replaceValue(self, 'UnlockedBrawlers', self.player.BrawlersUnlockedState)
                            break
                else:
                    self.writeVint(100) # Ammount
                    self.writeVint(16)
                    self.writeVint(BrawlersRewarded[i - 1])
                    self.writeVint(6)
                    
                    self.writeVint(0)
                    self.writeVint(0) # Reward end
                    self.writeVint(0)

            if totalreward >= 5:
                for index in range(4, totalreward):
                    for i in range(len(Boxes.reward_id)):
                        if Boxes.reward_id[i]['Name'] == reward[0]:
                            if reward[0] == "Gems" or reward[0] == "TokensDoubler":
                                self.writeVint(random.choice(BoxData[1][reward[0]])) # Reward ammount
                                self.writeVint(0)
                                self.writeVint(Boxes.reward_id[i]['ID']) # RewardID
                            else:
                                self.writeVint(random.randrange(BoxData[1]['Min' + reward[0]], BoxData[1]['Max' + reward[0]])) # Reward ammount
                                self.writeVint(0)
                                self.writeVint(Boxes.reward_id[i]['ID']) # RewardID
            
            # Box content end
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)

            newGold = self.player.gold + GoldValue
            DataBase.replaceValue(self, 'gold', newGold)

        if self.player.boxID == 3:
            OutOfSyncMessage(self.client, self.player, "Only big box work at the moment").send()

        if self.player.boxID == 1 or self.player.boxID == 10 :
            reward = random.choices(reward_list, weights=[7, 0.8, 0.7, 1])
            print(reward[0])
            BoxData = Boxes.boxes
            GoldValue = random.randrange(BoxData[1]['MinCoins'], BoxData[1]['MaxCoins'])

            if reward[0] == 0:
                totalreward = 4
            else:
                totalreward = 5

            if reward == 8:
                newGems = self.player.gems + 100
                DataBase.replaceValue(self, 'gems', newGems)
            elif reward == 3:
                newTickets = self.player.tickets + 100
                DataBase.replaceValue(self, 'tickets', newTickets)
            elif reward == 2:
                value = 100

            newBigBox = self.player.bigBoxes - 10
            DataBase.replaceValue(self, 'bigBoxes', newBigBox)

            self.writeVint(203)
            self.writeVint(0)
            self.writeVint(1)
            self.writeVint(12)
            self.writeVint(totalreward)
            
            self.writeVint(GoldValue)
            self.writeVint(0)
            self.writeVint(7)
            self.writeVint(0)

            self.writeVint(0)
            self.writeVint(0) # Reward end

            BrawlersRewarded = random.sample(unlocked_brawlers, k=3)
            for i in range(1, 4):
                if i == 3 and len(unlockable_brawlers) > 0:
                    for unlocked_brawlers in self.player.BrawlersUnlockedState:
                        if self.player.BrawlersUnlockedState[unlocked_brawlers] == 0:
                            
                            self.writeVint(1) # Reward ammount
                            self.writeVint(16) # Csv id
                            self.writeVint(int(unlocked_brawlers)) # Brawler id
                            self.writeVint(1) # Reward id

                            self.writeVint(0)
                            self.writeVint(0) # Reward end
                            self.writeVint(0)
                            self.player.BrawlersUnlockedState[unlocked_brawlers] = 1

                            DataBase.replaceValue(self, 'UnlockedBrawlers', self.player.BrawlersUnlockedState)
                            break

                else:
                    self.writeVint(100) # Ammount
                    self.writeVint(16)
                    self.writeVint(BrawlersRewarded[i - 1])
                    self.writeVint(6)
                    
                    self.writeVint(0)
                    self.writeVint(0) # Reward end
                    self.writeVint(0)

            if totalreward >= 5:
                for index in range(4, totalreward):
                    for i in range(len(Boxes.reward_id)):
                        if Boxes.reward_id[i]['Name'] == reward[0]:
                            if reward[0] == "Gems" or reward[0] == "TokensDoubler":
                                self.writeVint(random.choice(BoxData[1][reward[0]])) # Reward ammount
                                self.writeVint(0)
                                self.writeVint(Boxes.reward_id[i]['ID']) # RewardID
                            else:
                                self.writeVint(random.randrange(BoxData[1]['Min' + reward[0]], BoxData[1]['Max' + reward[0]])) # Reward ammount
                                self.writeVint(0)
                                self.writeVint(Boxes.reward_id[i]['ID']) # RewardID
            
            # Box content end
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)

            newGold = self.player.gold + GoldValue
            DataBase.replaceValue(self, 'gold', newGold)