from Utils.Writer import Writer
from Database.DataBase import DataBase


class OwnHomeDataMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24101
        self.player = player

    def encode(self):
        DataBase.loadAccount(self)

        self.writeVint(0)
        self.writeVint(0) # Timestamp

        self.writeVint(self.player.trophies) # Player Trophies
        self.writeVint(self.player.trophies) # Player Max Reached Trophies

        self.writeVint(122)
        self.writeVint(99)  # Trophy Road Reward

        self.writeVint(1262469) # Starting Level (exp points)

        self.writeScId(28, self.player.profileIcon ) # Player Icon ID
        self.writeScId(43, self.player.namecolor)    # Player Name Color ID

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

        self.writeVint(0)
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

        # Shop Offers

        items = [
            [6, 'Free Brawl Box', 0, 0],
            [14, 'Free Big Box', 0, 0],
            [10, 'Free Mega Box', 0, 0],
        ]
        count = len(items)

        self.writeVint(count) # Count
        for i in range(count):
            item = items[i]

            count2 = 1
            self.writeVint(count2) # Count2

            for i in range(count2):
                self.writeVint(item[0]) # Item Id
                self.writeVint(1)       # Multiplier
                self.writeVint(0)
                self.writeVint(item[3]) # Skin Id
                self.writeVint(0)

            self.writeVint(item[2]) # Cost
            self.writeVint(86400)   # Timer
            self.writeVint(1)       # "New" Offer
            self.writeVint(100)
            self.writeVint(0)

            self.writeBoolean(True)
            self.writeVint(0) # [0 = Normal, 1 = Daily Deals]
            self.writeBoolean(True)
            self.writeVint(0)

            self.writeInt(0)

            self.write_string_reference(item[1]) # Text

            self.writeBoolean(True)
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

        self.writeVint(1) # array
        for i in range(1):
            self.writeInt(7)
            self.writeInt(0)

        self.writeVint(0) # array
        self.writeVint(0) # array
        self.writeVint(0) # array

        self.writeBoolean(False)

        self.writeVint(2019049)
        self.writeVint(100)
        self.writeVint(10)

        self.writeVint(30)  # Shop Big Box price
        self.writeVint(3)

        self.writeVint(80)  # Shop Mega Box price
        self.writeVint(10)

        self.writeVint(50)  # Shop Token Doubler price
        self.writeVint(1000)# Shop Token Doubler amount

        self.writeVint(500)
        self.writeVint(50)
        self.writeVint(999900)

        self.writeVint(0) # array

        self.writeVint(8) # array
        for i in range(1, 8 + 1):
            self.writeVint(i)

        # Logic Events
        mapsList = [7, 32, 17, 0,  24, 202, 97, 167, 174]
        self.writeVint(8)  # map slots count

        for i in range(1, 8 + 1):

            self.writeVint(8 + i)
            self.writeVint(i)
            self.writeVint(0)
            self.writeVint(2802)
            self.writeVint(0)

            self.writeScId(15, int(mapsList[i - 1]) )

            self.writeVint(2)

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

        self.writeVint(4)
        for i in [20, 50, 140, 280]: # Gold price
            self.writeVint(i)

        self.writeVint(4)
        for i in [150, 400, 1200, 2600]: # Gold amount
            self.writeVint(i)

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
        self.writeInt(41000011) # theme ID
        self.writeInt(30)
        self.writeInt(1)

        self.writeVint(0) # array

        self.writeInt(0)
        self.writeInt(1)

        self.writeVint(0) # array

        self.writeVint(-64)

        self.writeBoolean(False)

        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)  # High Id
        self.writeVint(1)  # Low Id

        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)

        if self.player.name  == "Guest":
            self.writeString("Guest")  # player name
            self.writeVint(0)
            DataBase.createAccount(self)  # create new account
        else:
            self.writeString(self.player.name)  # player name
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
        self.writeVint(self.player.brawlBoxes)  # resource amount

        self.writeVint(5)  # csv id
        self.writeVint(8)  # resource id
        self.writeVint(self.player.gold)  # resource amount

        self.writeVint(5)  # csv id
        self.writeVint(9)  # resource id
        self.writeVint(self.player.bigBoxes)  # resource amount

        self.writeVint(5)  # csv id
        self.writeVint(10)  # resource id
        self.writeVint(self.player.starPoints)  # resource amount

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

















