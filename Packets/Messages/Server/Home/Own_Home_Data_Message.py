from datetime import datetime

from Utils.Writer import Writer
from Database.DataBase import DataBase

from Logic.Shop import Shop
from Logic.EventSlots import EventSlots


class OwnHomeDataMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24101
        self.player = player

    def encode(self):
        DataBase.loadAccount(self)

        self.writeVint(0)
        self.writeVint(int(datetime.timestamp(datetime.now()))) # Timestamp

        self.writeVint(self.player.trophies) # Player Trophies
        self.writeVint(self.player.trophies) # Player Max Reached Trophies

        self.writeVint(0)
        self.writeVint(95)  # Trophy Road Reward

        self.writeVint(500) # Starting Level (exp points)

        self.writeScId(28, self.player.profile_icon) # Player Icon ID
        self.writeScId(43, self.player.name_color)    # Player Name Color ID

        self.writeVint(0) # array

        # Selected Skins array
        self.writeVint(len(self.player.brawlers_skins))
        for brawler_id in self.player.brawlers_skins:
            self.writeVint(29)
            self.writeVint(self.player.brawlers_skins[brawler_id]) # skinID

        # Unlocked Skins array
        self.writeVint(len(self.player.skins_id))

        for skin_id in self.player.skins_id:
            self.writeScId(29, skin_id)

        self.writeVint(0) # array

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeBoolean(False)
        self.writeVint(1)
        self.writeBoolean(True)

        self.writeVint(0) # Remaining Tokens
        self.writeVint(0) # Season End Timer
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0) # array

        self.writeByte(8) # related to shop token doubler

        self.writeBoolean(True)
        self.writeBoolean(True)
        self.writeBoolean(True)

        self.writeVint(0)
        self.writeVint(0)

        # Shop Offers array

        count = len(Shop.offers)

        self.writeVint(count)
        for i in range(count):
            item = Shop.offers[i]

            self.writeVint(1)

            self.writeVint(item['ID'])
            self.writeVint(item['Multiplier'])
            self.writeVint(0)
            self.writeVint(item['SkinID'])
            self.writeVint(item['ShopType']) # [0 = Offer, 2 = Skins 3 = Star Shop]

            self.writeVint(item['Cost']) # Cost
            self.writeVint(item['Timer'])

            self.writeVint(1)
            self.writeVint(100)
            self.writeBoolean(False) # is Offer Purchased

            self.writeBoolean(False)
            self.writeVint(item['ShopDisplay']) # [0 = Normal, 1 = Daily Deals]
            self.writeBoolean(False)
            self.writeVint(0)

            self.writeInt(0)

            self.write_string_reference(item['OfferTitle'])

            self.writeBoolean(False)
            self.writeString()
            self.writeVint(0)
            self.writeBoolean(False)


        self.writeVint(0) # array

        self.writeVint(200) # Available Tokens
        self.writeVint(0)   # Time till Bonus Tokens (seconds)

        self.writeVint(0) # array

        self.writeVint(self.player.tickets) # Tickets
        self.writeVint(0)

        self.writeScId(16, self.player.brawler_id) # Selected Brawler

        self.writeString("RO") # Location
        self.writeString("26.165") # Supported Content Creator

        self.writeVint(0) # array
        self.writeVint(0) # array
        self.writeVint(0) # array
        self.writeVint(0) # array

        self.writeBoolean(False)

        self.writeVint(2019049)

        self.writeVint(100)
        self.writeVint(10)

        for item in Shop.boxes:
            self.writeVint(item['Cost'])
            self.writeVint(item['Multiplier'])

        self.writeVint(Shop.token_doubler['Cost'])
        self.writeVint(Shop.token_doubler['Amount'])

        self.writeVint(500)
        self.writeVint(50)
        self.writeVint(999900)

        self.writeVint(0) # array

        self.writeVint(8) # array
        for i in range(1, 8 + 1):
            self.writeVint(i)

        # Logic Events
        count = len(EventSlots.maps)
        self.writeVint(count)

        for map in EventSlots.maps:

            self.writeVint(8)
            self.writeVint(EventSlots.maps.index(map) + 1)
            self.writeVint(0)
            self.writeVint(2802)
            self.writeVint(0)

            self.writeScId(15, map['ID'])

            self.writeVint(map['Status'])

            self.writeString()
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)

        self.writeVint(0) # array

        # Logic Shop

        self.writeVint(8)
        for i in [20, 35, 75, 140, 290, 480, 800, 1250]:
            self.writeVint(i)

        self.writeVint(8)
        for i in [1, 2, 3, 4, 5, 10, 15, 20]:
            self.writeVint(i)

        self.writeVint(3)
        for i in [10, 30, 80]: # Tickets price
            self.writeVint(i)

        self.writeVint(3)
        for i in [6, 20, 60]: # Tickets amount
            self.writeVint(i)

        self.writeVint(len(Shop.gold))
        for item in Shop.gold:
            self.writeVint(item['Cost'])

        self.writeVint(len(Shop.gold))
        for item in Shop.gold:
            self.writeVint(item['Amount'])

        self.writeVint(2)

        self.writeVint(200) # Max Tokens
        self.writeVint(20)  # Plus Tokens

        self.writeVint(8640)
        self.writeVint(10)
        self.writeVint(5)

        self.writeByte(6)

        self.writeVint(50)
        self.writeVint(604800)

        self.writeBoolean(True)

        self.writeVint(0) # array

        self.writeVint(2) # Menu Theme
        self.writeInt(1)
        self.writeInt(41000011) # Theme ID
        self.writeInt(30)
        self.writeInt(1)

        self.writeVint(0) # array

        self.writeInt(0)
        self.writeInt(1)

        self.writeVint(0) # array

        self.writeVint(1)

        self.writeBoolean(True)

        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)  # High Id
        self.writeVint(1)  # Low Id

        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)

        if self.player.name  == "Guest":
            self.writeString("Guest")  # Player Name
            self.writeVint(0)
            DataBase.createAccount(self)
        else:
            self.writeString(self.player.name)  # Player Name
            self.writeVint(1)

        self.writeInt(0)

        self.writeVint(8)

        # Unlocked Brawlers & Resources array
        self.writeVint(len(self.player.card_unlock_id) + 4)  # count

        for unlock_id in self.player.card_unlock_id:
            self.writeVint(23)
            self.writeVint(unlock_id)
            self.writeVint(1)

        self.writeVint(5)  # csv id
        self.writeVint(1)  # resource id
        self.writeVint(self.player.brawl_boxes)  # resource amount

        self.writeVint(5)  # csv id
        self.writeVint(8)  # resource id
        self.writeVint(self.player.gold)  # resource amount

        self.writeVint(5)  # csv id
        self.writeVint(9)  # resource id
        self.writeVint(self.player.big_boxes)  # resource amount

        self.writeVint(5)  # csv id
        self.writeVint(10)  # resource id
        self.writeVint(self.player.star_points)  # resource amount


        # Brawlers Trophies array
        self.writeVint(len(self.player.brawlers_id))  # brawlers count

        for brawler_id in self.player.brawlers_id:
            self.writeScId(16, brawler_id)
            try:
                self.writeVint(self.player.brawlers_trophies[str(brawler_id)])
            except KeyError:
                self.player.brawlers_trophies.update({f'{brawler_id}': self.player.brawler_trophies_for_rank})
                DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
                self.writeVint(self.player.brawlers_trophies[str(brawler_id)])

        # Brawlers Trophies for Rank array
        self.writeVint(len(self.player.brawlers_id))  # brawlers count

        for brawler_id in self.player.brawlers_id:
            self.writeScId(16, brawler_id)
            try:
                self.writeVint(self.player.brawlers_trophies[str(brawler_id)])
            except KeyError:
                self.player.brawlers_trophies.update({f'{brawler_id}': self.player.brawler_trophies_for_rank})
                DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
                self.writeVint(self.player.brawlers_trophies[str(brawler_id)])

        self.writeVint(0)

        # Brawlers Upgrade Poitns array
        self.writeVint(len(self.player.brawlers_id))  # brawlers count

        for brawler_id in self.player.brawlers_id:
            self.writeScId(16, brawler_id)
            self.writeVint(self.player.brawler_upgrade_points)

        # Brawlers Power Level array
        self.writeVint(len(self.player.brawlers_id))  # brawlers count

        for brawler_id in self.player.brawlers_id:
            self.writeScId(16, brawler_id)
            self.writeVint(self.player.brawler_power_level)

        # Gadgets and Star Powers array
        self.writeVint(len(self.player.card_skills_id))  # count

        for skill_id in self.player.card_skills_id:
            self.writeVint(23)
            self.writeVint(skill_id)
            self.writeVint(1)

        # "New" Brawlers array
        self.writeVint(len(self.player.brawlers_id))  # brawlers count

        for brawler_id in self.player.brawlers_id:
            self.writeScId(16, brawler_id)
            self.writeVint(2)


        self.writeVint(self.player.gems) # Player Gems
        self.writeVint(self.player.gems)
        self.writeVint(1)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(2)
        self.writeVint(1585502369)