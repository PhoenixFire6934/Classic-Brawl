from Utils.Writer import Writer
from Database.DataBase import DataBase
from Utils.Helpers import Helpers


class OwnHomeDataMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24101
        self.player = player

    def encode(self):
        DataBase.loadAccount(self)

        self.writeVint(2020007)
        self.writeVint(75158) # Timestamp
            
        self.writeVint(self.player.trophies) # Player Trophies
        self.writeVint(self.player.highesttrophies) # Player Max Reached Trophies

        self.writeVint(0)
        self.writeVint(95)  # Trophy Road Reward

        self.writeVint(500) # Starting Level (exp points)

        self.writeScId(28, self.player.profileIcon) # Player Icon ID
        self.writeScId(43, self.player.namecolor) # Player Name Color ID
        
        self.writeVint(0) # array

        # Selected Skins array
        self.writeVint(len(self.player.brawlers_skins))
        for brawler_id in self.player.brawlers_skins:
            self.writeVint(29)
            self.writeVint(self.player.brawlers_skins[brawler_id]) # skinID

        # Unlocked Skins array
        self.writeVint(len(self.player.SkinsCount))

        for skin_id in self.player.SkinsCount:
            self.writeScId(29, skin_id)

        self.writeVint(0) # array

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeBoolean(False)  # "token limit reached message" if true

        self.writeVint(1)
        self.writeVint(1)

        self.writeVint(0) # Token doubler ammount

        self.writeVint(248791) # Season End Timer

        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(200)
        self.writeVint(200)

        self.writeVint(5)

        for i in [93, 206, 456, 1001, 2264]:
            self.writeVint(i)

        self.writeVint(8)

        self.writeVint(2)
        self.writeVint(2)
        self.writeVint(2)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0) # array

        self.writeVint(0) # array

        self.writeVint(200) # Available Tokens
        self.writeVint(0) # Time till Bonus Tokens (seconds)

        self.writeBoolean(True)  # Tickets enabled
        self.writeVint(0)
        self.writeVint(self.player.tickets)  # Tickets value
        self.writeVint(0)

        self.writeScId(16, self.player.brawlerID) # Selected Brawler

        self.writeString("RO")  # Location
        self.writeString("Classic Brawl") # Supported Content Creator


        self.writeVint(-133169153)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(2019053)

        self.writeVint(100)
        self.writeVint(10)

        self.writeVint(30)  # Shop Big Box price
        self.writeVint(3)

        self.writeVint(80)  # Shop Mega Box price
        self.writeVint(10)

        self.writeVint(50)  # Shop Token Doubler price
        self.writeVint(1000)# Shop Token Doubler amount


        self.writeVint(550)
        self.writeVint(0)
        self.writeVint(999900)

        self.writeVint(6) # count

        for i in range(6):
            self.writeVint(i)

        self.writeVint(15) # count

        for i in range(15):
            self.writeVint(i)


        totalSlots = 10
        mapsList = [7, 32, 17, 0,  24, 202, 97, 167, 174]
        self.writeVint(totalSlots -1 )  # map slots count

        for i in range(1, totalSlots):

            self.writeVint(-133000102)
            self.writeVint(i)
            self.writeVint(0)
            self.writeVint(75992) # Timer
            self.writeVint(10)

            self.writeScId(15, int(mapsList[i - 1]) ) # Game Mode Slot Map ID

            self.writeVint(3) # [3 = Nothing, 2 = Star Token, 1 = New Event]

            self.writeString()
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)

        # Shop
        self.writeVint(0)

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

        self.writeVint(200)# Max tokens
        self.writeVint(20) # Plus tokens

        self.writeVint(8640)
        self.writeVint(10)
        self.writeVint(5)

        self.writeVint(6)

        self.writeVint(50)
        self.writeVint(604800)

        self.writeBoolean(True) # Box boolean

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeInt(0)
        self.writeInt(1)

        self.writeVint(0)
        self.writeVint(-1)

        self.writeBoolean(False)

        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)  # High Id
        if self.player.LowID == 3486808210:
            self.player.LowID = Helpers.randomID(self)
            self.writeVint(self.player.LowID)
        else:
            self.writeVint(self.player.LowID)  # Low Id

        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)

        if self.player.name == "None":
            self.writeString("Guest")  # player name
            self.writeVint(0)
            DataBase.createAccount(self)  # create new account

        else:
            self.writeString(self.player.name)  # player name
            self.writeVint(1)

        self.writeVint(1207959551)


        # Unlocked Brawlers & Resources array
        self.writeVint(len(self.player.CardUnlockID) + 4) # count
        
        index = 0
        for unlock_id in self.player.CardUnlockID:
            self.writeVint(23)
            self.writeVint(unlock_id)
            self.writeVint(self.player.BrawlersUnlockedState[str(index)])

            if index == 34:
                index += 3
            elif index == 32:
                index += 2
            else:
                index += 1

        for resource in self.player.Resources:
            self.writeVint(5) # csv id
            self.writeVint(self.player.Resources[resource]['id']) # resource id
            self.writeVint(self.player.Resources[resource]['amount']) # resource amount


        # Brawlers Trophies array
        self.writeVint(len(self.player.BrawlersCount)) # brawlers count

        for brawler_id in self.player.BrawlersCount:
            self.writeScId(16, brawler_id)
            self.writeVint(self.player.BrawlersTrophies[str(brawler_id)])


        # Brawlers Trophies for Rank array
        self.writeVint(len(self.player.BrawlersCount))  # brawlers count

        for brawler_id in self.player.BrawlersCount:
            self.writeScId(16, brawler_id)
            self.writeVint(self.player.BrawlersTrophiesForRank[str(brawler_id)])

        self.writeVint(0)

       # Brawlers Upgrade Poitns array
        self.writeVint(len(self.player.BrawlersCount))  # brawlers count

        for brawler_id in self.player.BrawlersCount:
            self.writeScId(16, brawler_id)
            self.writeVint(self.player.brawler_upgrade_points)


        # Brawlers Power Level array
        self.writeVint(len(self.player.BrawlersCount))  # brawlers count

        for brawler_id in self.player.BrawlersCount:
            self.writeScId(16, brawler_id)
            self.writeVint(self.player.brawler_power_level)


        # Gadgets and Star Powers array
        self.writeVint(len(self.player.CardSkillsID))  # count

        for skill_id in self.player.CardSkillsID:
            self.writeVint(23)
            self.writeVint(skill_id)
            self.writeVint(1)


        # "new" Brawler Tag array
        self.writeVint(len(self.player.BrawlersCount))  # brawlers count

        for brawler_id in self.player.BrawlersCount:
            self.writeScId(16, brawler_id)
            if brawler_id == 31:
                self.writeVint(2)
            else:
                self.writeVint(0)

        self.writeVint(self.player.gems) # Player Gems
        self.writeVint(0)
        self.writeVint(99)
        self.writeVint(100)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(2)
        self.writeHexa('''A7 C6 98 F0 0B''')