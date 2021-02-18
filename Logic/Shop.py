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
            'ID': 6,
            'OfferTitle': 'SPECIAL OFFER',
            'Cost': 20,
            'Multiplier': 1,
            'SkinID': 0,
            'ShopType': 0,
            'ShopDisplay': 0,
            'Timer': 99999
        },

        {
            'ID': 10,
            'OfferTitle': 'SPECIAL OFFER',
            'Cost': 1500,
            'Multiplier': 1,
            'SkinID': 0,
            'ShopType': 3,
            'ShopDisplay': 0,
            'Timer': 99999
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


