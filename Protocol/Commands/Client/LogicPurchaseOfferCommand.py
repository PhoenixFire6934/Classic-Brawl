from ByteStream.Reader import Reader
from Logic.Home.LogicShopData import LogicShopData
from Protocol.Messages.Server.AvailableServerCommandMessage import AvailableServerCommandMessage
from Protocol.Commands.Server.LogicGiveDeliveryItemsCommand import LogicGiveDeliveryItemsCommand

class LogicPurchaseOfferCommand(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client
        self.offer_index: int = 0
        self.brawler: int = 0
        
        # Brawlers from the Road of Glory (not sold in the store)
        self.TrophyRoadBrawlers = [0, 1, 2, 3, 7, 8, 9, 14, 22, 27, 30]

    def decode(self):
        self.readVInt()
        self.readVInt()
        self.readLogicLong()

        self.offer_index = self.readVInt()

        self.brawler = self.readDataReference()[1]

    def process(self, db):
        offer_resource = LogicShopData.offers[self.offer_index].get("Currency", 0)
        offer_cost     = LogicShopData.offers[self.offer_index]["Cost"]

        if not LogicShopData.offers[self.offer_index].get("Claimed", False):

            self.player.delivery_items = {
                "DeliveryTypes": [100],
                'Items': []
            }

            for item in LogicShopData.offers[self.offer_index]["Items"]:
                if item["OfferID"] == 1:
                    delivery = {'Amount': item.get("Amount", 1), 'Value':7 }
                    self.player.delivery_items['Items'].append(delivery)
                    self.player.resources[1]['Amount'] += item.get("Amount", 1)
                    db.update_player_account(self.player.token, 'Resources', self.player.resources)

                elif item["OfferID"] == 4:
                    delivery = {"Amount": 1, "Value": 9, "ItemID": [29, item.get("ItemID", 0)]}
                    self.player.delivery_items['Items'].append(delivery)

                    if delivery["ItemID"][1] not in self.player.unlocked_skins:
                        self.player.unlocked_skins.append(delivery["ItemID"][1])
                        db.update_player_account(self.player.token, "UnlockedSkins", self.player.unlocked_skins)

                elif item["OfferID"] == 16:
                    delivery = {'Amount': item.get("Amount", 1), 'Value':8 }
                    self.player.delivery_items['Items'].append(delivery)

                    self.player.gems += item.get("Amount", 1)
                    db.update_player_account(self.player.token, 'Gems', self.player.gems)

                elif item["OfferID"] == 9:
                    delivery = {'Amount': item.get("Amount", 1), 'DataRef': [0, 0], 'Value':2 }
                    self.player.delivery_items['Items'].append(delivery)

                    self.player.token_doubler = self.player.token_doubler + item.get("Amount", 1)
                    db.update_player_account(self.player.token, 'TokenDoubler', self.player.token_doubler)

                elif item["OfferID"] == 3:
                    delivery = {'Amount': item.get("Amount", 1), 'DataRef': item.get("CharacterID", [16, 0]), 'Value':1 }
                    brawler_id = delivery["DataRef"][1]
                    
                    if brawler_id in self.TrophyRoadBrawlers:
                        print(f"Brawler {brawler_id} is a Trophy Road brawler, cannot be purchased!")
                        continue
                    
                    self.player.delivery_items['Items'].append(delivery)
                    if brawler_id not in self.player.brawlers_unlocked:
                        self.player.brawlers_unlocked.append(brawler_id)
                        db.update_player_account(self.player.token, 'UnlockedBrawlers', self.player.brawlers_unlocked)
                        
                        # Initializing trophies and levels for the new brawler
                        self.player.brawlers_trophies[str(brawler_id)] = 0
                        self.player.brawlers_high_trophies[str(brawler_id)] = 0
                        self.player.brawlers_level[str(brawler_id)] = 0
                        self.player.brawlers_powerpoints[str(brawler_id)] = 0
                        
                        db.update_player_account(self.player.token, 'BrawlersTrophies', self.player.brawlers_trophies)
                        db.update_player_account(self.player.token, 'BrawlersHighestTrophies', self.player.brawlers_high_trophies)
                        db.update_player_account(self.player.token, 'BrawlersLevel', self.player.brawlers_level)
                        db.update_player_account(self.player.token, 'BrawlersPowerPoints', self.player.brawlers_powerpoints)

                elif item["OfferID"] == 12:
                    delivery = {'Amount': item.get("Amount", 1), 'DataRef': [16, self.brawler], 'Value':6 }
                    self.player.delivery_items['Items'].append(delivery)

                    self.player.brawlers_powerpoints[str(self.brawler)] =+ item.get("Amount", 1)
                    db.update_player_account(self.player.token, 'BrawlersPowerPoints', self.player.brawlers_powerpoints)

                elif item["OfferID"] == 8:
                    delivery = {'Amount': item.get("Amount", 1), 'DataRef': item.get("CharacterID", [16, 0]), 'Value':6}
                    self.player.delivery_items['Items'].append(delivery)

                    self.player.brawlers_powerpoints[str(item.get("CharacterID", [16, 0]))] += item.get("Amount", 1)
                    db.update_player_account(self.player.token, 'BrawlersPowerPoints', self.player.brawlers_powerpoints)

                elif item["OfferID"] in [0, 6]:
                    for i in range(item["Amount"]): self.player.delivery_items["DeliveryTypes"].append(10)
                    self.player.delivery_items['Count'] = item.get("Amount", 1)

                elif item["OfferID"] == 14:
                    for i in range(item["Amount"]): self.player.delivery_items["DeliveryTypes"].append(12)
                    self.player.delivery_items['Count'] = item.get("Amount", 1)

                elif item["OfferID"] == 10:
                    for i in range(item["Amount"]): self.player.delivery_items["DeliveryTypes"].append(11)
                    self.player.delivery_items['Count'] = item.get("Amount", 1)

                else:
                    print(f"Unsupported offer ID: {item['OfferID']}")

            if offer_resource == 0:
                self.player.gems -= offer_cost
                db.update_player_account(self.player.token, 'Gems', self.player.gems)

            elif offer_resource == 1:
                self.player.resources[1]['Amount'] -= offer_cost
                db.update_player_account(self.player.token, 'Resources', self.player.resources)

            elif offer_resource == 3:
                self.player.resources[3]['Amount'] -= offer_cost
                db.update_player_account(self.player.token, 'Resources', self.player.resources)

            self.player.db = db

            AvailableServerCommandMessage(self.client, self.player, LogicGiveDeliveryItemsCommand).send()