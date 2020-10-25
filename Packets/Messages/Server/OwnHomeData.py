from Utils.Writer import Writer
from database.DataBase import DataBase


class OwnHomeData(Writer):

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
        self.writeVint(100)  # reward for trophy road

        self.writeVint(1262469)  # starting level (exp points)

        self.writeVint(28)
        self.writeVint(self.player.profileIcon)  # player icon ID

        self.writeVint(43)
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

        for i in range(0,6):
            self.writeVint(0)

        self.writeVint(0)  # "token limit reached message" if true

        self.writeVint(1)
        self.writeVint(1)
        self.writeVint(0)
        self.writeVint(248791)
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
        self.writeVint(1140)

        self.writeBoolean(True)  # tickets enabled
        self.writeVint(0)
        self.writeVint(self.player.tickets)  # tickets number
        self.writeVint(-21)
        self.writeVint(16)

        self.writeVint(self.player.brawlerID)

        self.writeString("RO")  # location
        self.writeString("") # supported content creator

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

        totalSlots = 9
        mapsList = [7, 32, 17, 24, 0, 202, 97, 167, 174]
        self.writeVint(totalSlots)  # map slots count

        for i in range(0, totalSlots):

            self.writeVint(-133000102)  # map slot starts here
            self.writeVint(i)
            self.writeVint(0)
            self.writeVint(75992)
            self.writeVint(10)
            self.writeVint(15)

            self.writeVint(int(mapsList[i]))  # game mode slot map id

            self.writeVint(3)
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


        self.writeVint(0)
        self.writeVint(8)
        self.writeVint(20)
        self.writeVint(35)
        self.writeVint(75)

        self.writeVint(140)
        self.writeVint(290)
        self.writeVint(480)
        self.writeVint(800)
        self.writeVint(1250)

        self.writeVint(8)
        self.writeVint(1)
        self.writeVint(2)
        self.writeVint(3)
        self.writeVint(4)
        self.writeVint(5)
        self.writeVint(10)
        self.writeVint(15)
        self.writeVint(20)
        self.writeVint(3)
        self.writeVint(10)

        self.writeVint(30)
        self.writeVint(80)

        self.writeVint(3)
        self.writeVint(6)
        self.writeVint(20)
        self.writeVint(60)

        self.writeVint(4)

        self.writeVint(20)  # first coin pack price
        self.writeVint(50)  # second coin pack price
        self.writeVint(140)  # third coin pack price
        self.writeVint(280)  # fourth coin pack price

        self.writeVint(4)

        self.writeVint(150)  # first coin pack amount
        self.writeVint(400)  # second coin pack amount
        self.writeVint(1200)  # third  coin pack amount
        self.writeVint(2600)  # fourth  coin pack amount

        self.writeVint(2)
        self.writeVint(200)
        self.writeVint(20)
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

        self.writeVint(0)  # Low Id
        self.writeVint(1)  # High Id

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

        self.writeVint(38) # brawlers count


        i = 0

        for x in range(0,19):
            self.writeVint(23)
            self.writeVint(i)
            self.writeVint(1)
            i += 4
        
        i = 95

        for x in range(0,8):
            self.writeVint(23)
            self.writeVint(i)
            self.writeVint(1)
            i += 5      
        
        i = 177

        for x in range(0,2):
            self.writeVint(23)
            self.writeVint(i)
            self.writeVint(1)
            i += 5 

        i = 188

        for x in range(0,4):
            self.writeVint(23)
            self.writeVint(i)
            self.writeVint(1)
            i += 6

        i = 218

        for x in range(0,2):
            self.writeVint(23)
            self.writeVint(i)
            self.writeVint(1)
            i += 18            


        self.writeVint(5)
        self.writeVint(1)


        self.writeVint(99999)  # brawl box tokens (100 tokens = 1 brawl box)
        self.writeVint(5)

        self.writeVint(8)
        self.writeVint(self.player.gold)  # gold
        self.writeVint(5)
        
        self.writeVint(9)
        self.writeVint(99999)  # big box tokens (10 tokens = 1 big box)


        # brawlers trophies 
        self.writeVint(35)  # brawlers count

        for i in range(0, 32):
            self.writeVint(16)
            self.writeVint(i)
            self.writeVint(99999)
        # exceptions
        self.writeVint(16)
        self.writeVint(32)
        self.writeVint(99999)  # max trophies
        self.writeVint(16)
        self.writeVint(34)
        self.writeVint(99999)  # jacky trophies
        self.writeVint(16)
        self.writeVint(37)
        self.writeVint(99999)  # sprout trophies


        # brawlers trophies for rank
        self.writeVint(35)  # brawlers count

        for i in range(0,32):
            self.writeVint(16)
            self.writeVint(i)
            self.writeVint(99999)
        # exceptions
        self.writeVint(16)
        self.writeVint(32)
        self.writeVint(99999)  # max trophies for rank
        self.writeVint(16)
        self.writeVint(34)
        self.writeVint(99999)  # jacky trophies for rank
        self.writeVint(16)
        self.writeVint(37)
        self.writeVint(99999)  # sprout trophies for rank

        self.writeVint(0)

       # unkown part
        self.writeVint(35)  # brawlers count

        for i in range(0,32):
            self.writeVint(16)
            self.writeVint(i)
            self.writeVint(1440)  # hmm what could this be?
        self.writeVint(16)
        self.writeVint(32)
        self.writeVint(1440)
        self.writeVint(16)
        self.writeVint(34)
        self.writeVint(1440)
        self.writeVint(16)
        self.writeVint(37)
        self.writeVint(1440)


        # brawlers power level
        self.writeVint(35)  # brawlers count

        for i in range(0,32):
            self.writeVint(16)
            self.writeVint(i)
            self.writeVint(8)  # shelly power level (value shows in game +1, so value 8 = power 9)

        self.writeVint(16)
        self.writeVint(32)
        self.writeVint(8)  # max power level
        self.writeVint(16)
        self.writeVint(34)
        self.writeVint(8)  # jacky power level
        self.writeVint(16)
        self.writeVint(37)
        self.writeVint(8)  # sprout power level


        self.writeVint(119)  # gadgets and star powers


        for i in range(76, 95):
 

            self.writeVint(23)
            self.writeVint(i)
            self.writeVint(1)

        self.writeVint(23)
        self.writeVint(99)
        self.writeVint(1)

        self.writeVint(23)
        self.writeVint(104)
        self.writeVint(1)   
        
        i = 109

        for x in range(0, 5):


            self.writeVint(23)
            self.writeVint(i)
            self.writeVint(1)
            i+=5

        for i in range(134, 172):


            self.writeVint(23)
            self.writeVint(i)
            self.writeVint(1) 


        self.writeVint(23)
        self.writeVint(172)
        self.writeVint(1)


        for i in range(174, 176):


            self.writeVint(23)
            self.writeVint(i)
            self.writeVint(1) 



        self.writeVint(23)
        self.writeVint(181)
        self.writeVint(1)
        self.writeVint(23)

        self.writeVint(186)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(187)
        self.writeVint(1)

        self.writeVint(23)
        self.writeVint(192)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(193)
        self.writeVint(1)
        self.writeVint(23)

        self.writeVint(198)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(199)
        self.writeVint(1)
        self.writeVint(23)

        self.writeVint(204)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(205)
        self.writeVint(1)
        self.writeVint(23)

        self.writeVint(210)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(211)
        self.writeVint(1)

        self.writeVint(23)
        self.writeVint(216)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(217)
        self.writeVint(1)


        for i in range(222, 224):
            self.writeVint(23)
            self.writeVint(i)
            self.writeVint(1)
        
        for i in range(240, 277):
            self.writeVint(23)
            self.writeVint(i)
            self.writeVint(1)



        # "new" brawler tag
        self.writeVint(35)  # brawlers count

        for i in range(0, 33):
 
            self.writeVint(16)
            self.writeVint(i)
            self.writeVint(2)  # mr p  "new" tag           

        # exceptions
        self.writeVint(16)
        self.writeVint(34)
        self.writeVint(2)  # jacky "new" tag
        self.writeVint(16)
        self.writeVint(37)
        self.writeVint(2) # sprout "new" tag


        self.writeVint(self.player.gems) # gems
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(100)

        for i in range(0, 7):
            self.writeVint(0)

        self.writeVint(2)
        self.writeVint(1550832808)
        self.writeVint(-1040385)

        for i in range(0, 4):
            self.writeVint(0)

        self.writeVint(-33)
        self.writeVint(-49)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(2)
        for i in range(0, 4):
            self.writeVint(0)

        self.writeVint(-1040385)

        for i in range(0, 4):
            self.writeVint(0)



