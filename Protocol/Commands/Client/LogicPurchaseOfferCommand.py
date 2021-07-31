from ByteStream.Reader import Reader
from Logic.Home.LogicShopData import LogicShopData
from Protocol.Messages.Server.AvailableServerCommandMessage import AvailableServerCommandMessage

class LogicPurchaseOfferCommand(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.readVInt()
        self.readVInt()
        self.readLogicLong()

        self.offer_index = self.readVInt()

        self.brawler = self.readDataReference()[1]

    def process(self, db):
        offer_id       = LogicShopData.offers[self.offer_index]['OfferID']
        offer_resource = LogicShopData.offers[self.offer_index]['ShopType']
        offer_cost     = LogicShopData.offers[self.offer_index]['Cost']
        offer_amount   = LogicShopData.offers[self.offer_index]['Multiplier']
        offer_char = LogicShopData.offers[self.offer_index]['DataReference'][1]

        if not LogicShopData.offers[self.offer_index]['Claimed']:


            self.player.delivery_items = {
                'Count': 1,
                'Type': 0,
                'Items': []
            }

            if offer_id == 1:
                item = {'Amount': offer_amount, 'DataRef': [0, 0], 'Value':7 }
                self.player.delivery_items['Type'] = 100
                self.player.delivery_items['Items'].append(item)

                self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + offer_amount
                db.update_player_account(self.player.token, 'Resources', self.player.resources)
                LogicShopData.offers[self.offer_index]['Claimed'] = True


            elif offer_id == 16:
                item = {'Amount': offer_amount, 'DataRef': [0, 0], 'Value':8 }
                self.player.delivery_items['Type'] = 100
                self.player.delivery_items['Items'].append(item)

                self.player.gems = self.player.gems + offer_amount
                db.update_player_account(self.player.token, 'Gems', self.player.gems)
                LogicShopData.offers[self.offer_index]['Claimed'] = True

            elif offer_id == 9:
                item = {'Amount': offer_amount, 'DataRef': [0, 0], 'Value':2 }
                self.player.delivery_items['Type'] = 100
                self.player.delivery_items['Items'].append(item)

                self.player.token_doubler = self.player.token_doubler + offer_amount
                db.update_player_account(self.player.token, 'TokenDoubler', self.player.token_doubler)
                LogicShopData.offers[self.offer_index]['Claimed'] = True

            elif offer_id == 3:
                item = {'Amount': offer_amount, 'DataRef': [16, offer_char ], 'Value':1 }
                self.player.delivery_items['Type'] = 100
                self.player.delivery_items['Items'].append(item)
                if offer_char not in self.player.brawlers_unlocked:
                    self.player.brawlers_unlocked.append(offer_char)
                    db.update_player_account(self.player.token, 'UnlockedBrawlers', self.player.brawlers_unlocked)
                LogicShopData.offers[self.offer_index]['Claimed'] = True

            elif offer_id == 12:
                item = {'Amount': offer_amount, 'DataRef': [16, self.brawler ], 'Value':6 }
                self.player.delivery_items['Type'] = 100
                self.player.delivery_items['Items'].append(item)

                self.player.brawlers_powerpoints[str(self.brawler)] = self.player.brawlers_powerpoints[str(self.brawler)] + offer_amount
                db.update_player_account(self.player.token, 'BrawlersPowerPoints', self.player.brawlers_powerpoints)
                LogicShopData.offers[self.offer_index]['Claimed'] = True


            elif offer_id == 8:
                item = {'Amount': offer_amount, 'DataRef': [16, offer_char ], 'Value':6 }
                self.player.delivery_items['Type'] = 100
                self.player.delivery_items['Items'].append(item)

                self.player.brawlers_powerpoints[str(offer_char)] = self.player.brawlers_powerpoints[str(offer_char)] + offer_amount
                db.update_player_account(self.player.token, 'BrawlersPowerPoints', self.player.brawlers_powerpoints)
                LogicShopData.offers[self.offer_index]['Claimed'] = True

            elif offer_id in [0, 6]:
                self.player.delivery_items['Type'] = 10
                self.player.delivery_items['Count'] = offer_amount
                LogicShopData.offers[self.offer_index]['Claimed'] = True


            elif offer_id == 14:
                self.player.delivery_items['Type'] = 12
                self.player.delivery_items['Count'] = offer_amount
                LogicShopData.offers[self.offer_index]['Claimed'] = True


            elif offer_id == 10:
                self.player.delivery_items['Type'] = 11
                self.player.delivery_items['Count'] = offer_amount
                LogicShopData.offers[self.offer_index]['Claimed'] = True

            else:
                print(f"Unsupported offer ID: {offer_id}")


            if offer_resource == 0:
                self.player.gems = self.player.gems - offer_cost
                db.update_player_account(self.player.token, 'Gems', self.player.gems)

            elif offer_resource == 1:
                self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] - offer_cost
                db.update_player_account(self.player.token, 'Resources', self.player.resources)

            elif offer_resource == 3:
                self.player.resources[3]['Amount'] = self.player.resources[3]['Amount'] - offer_cost
                db.update_player_account(self.player.token, 'Resources', self.player.resources)

            self.player.db = db

            AvailableServerCommandMessage(self.client, self.player, 203).send()



