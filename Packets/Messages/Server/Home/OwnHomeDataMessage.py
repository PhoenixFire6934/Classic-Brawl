from Utils.Writer import Writer
from Database.DataBase import DataBase


class OwnHomeDataMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24101
        self.player = player

    def encode(self):
        DataBase.loadAccount(self)

        self.writeVint(2020007)
        self.writeVint(75158) # timestamp

        self.writeVint(self.player.trophies) # trophies
        self.writeVint(self.player.trophies) # max reached trophies

        self.writeVint(122)
        self.writeVint(99)  # reward for trophy road

        self.writeVint(1262469)  # starting level (exp points)

        self.writeVint(28) # csv id
        self.writeVint(self.player.profileIcon)  # player icon ID

        self.writeVint(43) # csv id
        self.writeVint(self.player.namecolor)  # player name color ID

        self.writeVint(9)
        self.writeVint(0)
        self.writeVint(2)
        self.writeVint(3)
        self.writeVint(5)
        self.writeVint(6)
        self.writeVint(7)
        self.writeVint(8)
        self.writeVint(9)
        self.writeVint(10)

        self.writeVint(3)
        self.writeVint(29)

        self.writeVint(14)
        self.writeVint(29)

        self.writeVint(self.player.skinID) # skinID
        self.writeVint(29)

        self.writeVint(0)


        self.writeVint(len(self.player.SkinsCount)) # unlocked skins array

        for skin_id in self.player.SkinsCount:
            self.writeScId(29, skin_id)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeBoolean(False)  # "token limit reached message" if true

        self.writeVint(1)
        self.writeVint(1)
        self.writeVint(0)

        self.writeVint(248791) # season ends timer

        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(200)
        self.writeVint(200)

        self.writeVint(5)
        self.writeVint(93)
        self.writeVint(206)
        self.writeVint(456)
        self.writeVint(1001)
        self.writeVint(2264)
        self.writeVint(8)
        self.writeVint(2)
        self.writeVint(2)
        self.writeVint(2)

        for i in range(0,4):
            self.writeVint(0)

        self.writeVint(100) # available tokens
        self.writeVint(99999) # time till bonus tokens (seconds)

        self.writeBoolean(True)  # tickets enabled
        self.writeVint(0)
        self.writeVint(self.player.tickets)  # tickets number
        self.writeVint(-21)
        self.writeVint(16)

        self.writeVint(self.player.brawlerID) # selected brawler

        self.writeString("RO")  # location
        self.writeString("26.165") # supported content creator

        self.writeVint(-133169153)

        for i in range(0,4):
            self.writeVint(0)

        self.writeVint(2019053)
        self.writeVint(100)

        self.writeVint(10)
        self.writeVint(30)  # shop big box price

        self.writeVint(3)
        self.writeVint(80)  # shop mega box price

        self.writeVint(10)
        self.writeVint(50)  # shop token doubler price
        self.writeVint(1000)  # shop token doubler amount

        self.writeVint(500)
        self.writeVint(50)
        self.writeVint(999900)


        self.writeVint(6)
        self.writeVint(0)
        self.writeVint(30)
        self.writeVint(80)
        self.writeVint(170)
        self.writeVint(350)
        self.writeVint(0)
        self.writeVint(15)

        for i in range(0,10):
            self.writeVint(i)

        for i in range(20, 25):
            self.writeVint(i)

        totalSlots = 10
        mapsList = [7, 32, 17, 0,  24, 202, 97, 167, 174]
        self.writeVint(totalSlots -1 )  # map slots count

        for i in range(1, totalSlots):

            self.writeVint(-133000102)  # map slot starts here
            self.writeVint(i)
            self.writeVint(0)
            self.writeVint(75992) # timer
            self.writeVint(10)
            self.writeVint(15)

            self.writeVint(int(mapsList[i - 1]))  # game mode slot map id

            self.writeVint(2) # [3 = nothing, 2 = star token, 1 = new event]
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)  # map slot ends here

        # shop
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

        self.writeVint(999) # max tokens
        self.writeVint(20) # plus tokens

        self.writeVint(8640)
        self.writeVint(10)
        self.writeVint(5)
        self.writeVint(6)
        self.writeVint(50)
        self.writeVint(604800)
        self.writeVint(1)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(14)
        self.writeVint(0)
        self.writeVint(3193)

        self.writeVint(-8)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)  # High Id
        self.writeVint(1)  # Low Id

        for i in range(0, 4):
            self.writeVint(0)

        if self.player.name is None:

            self.writeString("Guest")  # player name
            self.writeVint(0)
            DataBase.createAccount(self)  # create new account

        else:
            self.writeString(self.player.name)  # player name
            self.writeVint(1)


        self.writeVint(1207959551)


        # Unlocked Brawlers & Resources array
        self.writeVint(len(self.player.CardUnlockID) + 4) # count

        for unlock_id in self.player.CardUnlockID:
            self.writeVint(23)
            self.writeVint(unlock_id)
            self.writeVint(1)



        for resource in self.player.Resources:
            self.writeVint(5) # csv id
            self.writeVint(self.player.Resources[resource]['id']) # resource id
            self.writeVint(self.player.Resources[resource]['amount']) # resource amount



        # Brawlers Trophies array
        self.writeVint(len(self.player.BrawlersCount)) # brawlers count

        for brawler_id in self.player.BrawlersCount:
            self.writeScId(16, brawler_id)
            self.writeVint(self.player.brawler_trophies)



        # Brawlers Trophies for Rank array
        self.writeVint(len(self.player.BrawlersCount))  # brawlers count

        for brawler_id in self.player.BrawlersCount:
            self.writeScId(16, brawler_id)
            self.writeVint(self.player.brawler_trophies_for_rank)

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


        # "new" brawler tag
        self.writeVint(len(self.player.BrawlersCount))  # brawlers count

        for brawler_id in self.player.BrawlersCount:
            self.writeScId(16, brawler_id)
            self.writeVint(2)



        self.writeVint(self.player.gems) # gems
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(100)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(2)
        self.writeVint(0)




