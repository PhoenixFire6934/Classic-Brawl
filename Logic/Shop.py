class Shop:
    """
    << Shop Offers IDs List >>

    0 = Free Brawl Box
    1 = Gold
    2 = Random Brawler
    3 = Brawler
    4 = Skin
    5 = StarPower/ Gadget
    6 = Brawl Box
    7 = Tickets
    8 = Power Points (for a specific brawler)
    9 = Token Doubler
    10 = Mega Box
    11 = Keys (???)
    12 = Power Points
    13 = EventSlot (???)
    14 = Big Box
    15 = AdBox (not working anymore)
    16 = Gems

    """



    offers = [

        {
            'ID': 4,
            'OfferTitle': 'Coins',
            'Cost': 2,
            'Multiplier': 1,
            'SkinID': 52,
            'ShopType': 6,
            'ShopDisplay': 0,
            'Timer': 69420
        },
        
        {
            'ID': 10,
            'OfferTitle': 'Coins',
            'Cost': 20,
            'Multiplier': 1,
            'SkinID': 0,
            'ShopType': 0,
            'ShopDisplay': 1,
            'Timer': 69420
        },


    ]


    gold = [
        {
            'Cost': 20,
            'Amount': 150
        },

        {
            'Cost': 50,
            'Amount': 400
        },

        {
            'Cost': 140,
            'Amount': 1200
        }

    ]

    boxes = [
        {
            'Name': 'Big Box',
            'Cost': 30,
            'Multiplier': 3
        },

        {
            'Name': 'Mega Box',
            'Cost': 80,
            'Multiplier': 10
        }

    ]


    token_doubler = {

        'Cost': 50,
        'Amount': 1000
    }


    def EncodeShopOffers(self):
        count = len(Shop.offers)
        self.writeVint(count)
        for i in range(count):
            item = Shop.offers[i]

            self.writeVint(1)

            self.writeVint(item['ID']) # ItemID
            self.writeVint(item['Multiplier']) # Ammount
            self.writeVint(0)
            self.writeVint(item['SkinID'])
            self.writeVint(item['ShopType'])  # [0 = Offer, 2 = Skins 3 = Star Shop]

            self.writeVint(item['Cost'])  # Cost
            self.writeVint(item['Timer']) # Timer

            self.writeVint(1)
            self.writeVint(100)
            self.writeVint(0)  # is Offer Purchased

            self.writeBoolean(True)
            self.writeVint(item['ShopDisplay'])  # [0 = Normal, 1 = Daily Deals]
            self.writeBoolean(True)
            self.writeInt(0)