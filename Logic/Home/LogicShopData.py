import json
from datetime import datetime

class LogicShopData:

    shop_resources = json.loads(open('shop.json', 'r').read())

    gold_packs = shop_resources['GoldPacks']
    gold_cost, gold_amount = [], []

    for x in gold_packs:
        gold_cost.append(x['Cost'])
        gold_amount.append(x['Amount'])

    boxes = shop_resources['Boxes']
    token_doubler = shop_resources['TokenDoubler']

    offers = shop_resources['Offers']

    def encodeShopPacks(self):
        # Unknown
        self.writeArrayVint([20, 35, 75, 140, 290, 480, 800, 1250])
        self.writeArrayVint([1, 2, 3, 4, 5, 10, 15, 20])
        # Tickets
        self.writeArrayVint([10, 30, 80])
        self.writeArrayVint([6, 20, 60])
        # Gold
        self.writeArrayVint(LogicShopData.gold_cost)
        self.writeArrayVint(LogicShopData.gold_amount)

    def encodeShopResources(self):
        time_stamp = int(datetime.timestamp(datetime.now()))

        self.writeVInt(time_stamp)
        LogicShopData.encodeBoxes(self)
        LogicShopData.encodeTokenDoubler(self)


    def encodeShopOffers(self):
        self.writeVInt(len(LogicShopData.offers))
        for x in LogicShopData.offers:
            self.writeVInt(1) # array
            for y in range(1):
                self.writeVInt(x['OfferID'])
                self.writeVInt(x['Multiplier'])
                self.writeDataReference(x['DataReference'][0], x['DataReference'][1])
                self.writeVInt(0)

            self.writeVInt(x['ShopType'])

            self.writeVInt(x['Cost'])
            self.writeVInt(x['Timer'])

            self.writeVInt(1)
            self.writeVInt(100)
            self.writeUInt8(0)

            self.writeUInt8(0)
            self.writeVInt(x['ShopDisplay'])
            self.writeUInt8(0)
            self.writeVInt(0)

            self.writeInt(0)
            self.writeStringReference(x['OfferText'])

            self.writeUInt8(0)
            self.writeString()
            self.writeVInt(0)
            self.writeUInt8(0)
            # self.writeVInt(2)
            # self.writeVInt(0)




    def encodeBoxes(self):
        self.writeVInt(100) # Tokens for 1 Brawl Box
        self.writeVInt(10)  # Tokens for 1 Big Box

        self.writeVInt(LogicShopData.boxes[0]['Cost'])
        self.writeVInt(LogicShopData.boxes[0]['Multiplier'])

        self.writeVInt(LogicShopData.boxes[1]['Cost'])
        self.writeVInt(LogicShopData.boxes[1]['Multiplier'])


    def encodeTokenDoubler(self):
        self.writeVInt(LogicShopData.token_doubler[0]['Cost'])
        self.writeVInt(LogicShopData.token_doubler[0]['Amount'])
