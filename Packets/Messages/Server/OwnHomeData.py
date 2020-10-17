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

        self.writeVint(0)  # "token limit reached message" if 1
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
        self.writeVint(1)
        self.writeVint(2)
        self.writeVint(3)
        self.writeVint(4)
        self.writeVint(5)
        self.writeVint(6)
        self.writeVint(7)
        self.writeVint(8)
        self.writeVint(9)
        self.writeVint(10)
        self.writeVint(20)
        self.writeVint(21)
        self.writeVint(22)
        self.writeVint(23)
        self.writeVint(24)

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
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
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

        self.writeVint(23)
        self.writeVint(0)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(4)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(8)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(12)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(16)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(20)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(24)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(28)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(32)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(36)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(40)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(44)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(48)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(52)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(56)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(60)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(64)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(68)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(72)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(95)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(100)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(105)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(110)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(115)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(120)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(125)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(130)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(177)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(182)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(188)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(194)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(200)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(206)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(218)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(236)
        self.writeVint(1)
        self.writeVint(5)
        self.writeVint(1)


        self.writeVint(99999)  # brawl box tokens (100 tokens = 1 brawl box)
        self.writeVint(5)

        self.writeVint(8)
        self.writeVint(self.player.gold)  # gold
        self.writeVint(5)
        
        self.writeVint(9)
        self.writeVint(99999)  # big box tokens (10 tokens = 1 big box)

        self.writeVint(35)  # brawlers count

        self.writeVint(16)
        self.writeVint(0)
        self.writeVint(99999)  # shelly trophies
        self.writeVint(16)
        self.writeVint(1)
        self.writeVint(99999)  # colt trophies
        self.writeVint(16)
        self.writeVint(2)
        self.writeVint(99999)  # bull trophies
        self.writeVint(16)
        self.writeVint(3)
        self.writeVint(99999)  # brock trophies
        self.writeVint(16)
        self.writeVint(4)
        self.writeVint(99999)  # rico trophies
        self.writeVint(16)
        self.writeVint(5)
        self.writeVint(99999)  # spike trophies
        self.writeVint(16)
        self.writeVint(6)
        self.writeVint(99999)  # barley trophies
        self.writeVint(16)
        self.writeVint(7)
        self.writeVint(99999)  # jessie trophies
        self.writeVint(16)
        self.writeVint(8)
        self.writeVint(99999)  # nita trophies
        self.writeVint(16)
        self.writeVint(9)
        self.writeVint(99999)  # dynamike trophies
        self.writeVint(16)
        self.writeVint(10)
        self.writeVint(99999)  # primo trophies
        self.writeVint(16)
        self.writeVint(11)
        self.writeVint(99999)  # mortis trophies
        self.writeVint(16)
        self.writeVint(12)
        self.writeVint(99999)  # crow trophies
        self.writeVint(16)
        self.writeVint(13)
        self.writeVint(99999)  # poco trophies
        self.writeVint(16)
        self.writeVint(14)
        self.writeVint(99999)  # bo trophies
        self.writeVint(16)
        self.writeVint(15)
        self.writeVint(99999)  # piper trophies
        self.writeVint(16)
        self.writeVint(16)
        self.writeVint(99999)  # pam trophies
        self.writeVint(16)
        self.writeVint(17)
        self.writeVint(99999)  # tara trophies
        self.writeVint(16)
        self.writeVint(18)
        self.writeVint(99999)  # darryl trophies
        self.writeVint(16)
        self.writeVint(19)
        self.writeVint(99999)  # penny trophies
        self.writeVint(16)
        self.writeVint(20)
        self.writeVint(99999)  # frank trophies
        self.writeVint(16)
        self.writeVint(21)
        self.writeVint(99999)  # gene trophies
        self.writeVint(16)
        self.writeVint(22)
        self.writeVint(99999)  # tick trophies
        self.writeVint(16)
        self.writeVint(23)
        self.writeVint(99999)  # leon trophies
        self.writeVint(16)
        self.writeVint(24)
        self.writeVint(99999)  # rosa trophies
        self.writeVint(16)
        self.writeVint(25)
        self.writeVint(99999)  # carl trophies
        self.writeVint(16)
        self.writeVint(26)
        self.writeVint(99999)  # bibi trophies
        self.writeVint(16)
        self.writeVint(27)
        self.writeVint(99999)  # 8bit trophies
        self.writeVint(16)
        self.writeVint(28)
        self.writeVint(99999)  # sandy trophies
        self.writeVint(16)
        self.writeVint(29)
        self.writeVint(99999)  # bea trophies
        self.writeVint(16)
        self.writeVint(30)
        self.writeVint(99999)  # emz trophies
        self.writeVint(16)
        self.writeVint(31)
        self.writeVint(99999)  # mr p trophies
        self.writeVint(16)
        self.writeVint(32)
        self.writeVint(99999)  # max trophies
        self.writeVint(16)
        self.writeVint(34)
        self.writeVint(99999)  # jacky trophies
        self.writeVint(16)
        self.writeVint(37)
        self.writeVint(99999)  # sprout trophies

        self.writeVint(35)  # brawlers count

        self.writeVint(16)
        self.writeVint(0)
        self.writeVint(99999)  # shelly trophies for rank
        self.writeVint(16)
        self.writeVint(1)
        self.writeVint(99999)  # colt trophies for rank
        self.writeVint(16)
        self.writeVint(2)
        self.writeVint(99999)  # bull trophies for rank
        self.writeVint(16)
        self.writeVint(3)
        self.writeVint(99999)  # brock trophies for rank
        self.writeVint(16)
        self.writeVint(4)
        self.writeVint(99999)  # rico trophies for rank
        self.writeVint(16)
        self.writeVint(5)
        self.writeVint(99999)  # spike trophies for rank
        self.writeVint(16)
        self.writeVint(6)
        self.writeVint(99999)  # barley trophies for rank
        self.writeVint(16)
        self.writeVint(7)
        self.writeVint(99999)  # jessie trophies for rank
        self.writeVint(16)
        self.writeVint(8)
        self.writeVint(99999)  # nita trophies for rank
        self.writeVint(16)
        self.writeVint(9)
        self.writeVint(99999)  # dynamike trophies for rank
        self.writeVint(16)
        self.writeVint(10)
        self.writeVint(99999)  # primo trophies for rank
        self.writeVint(16)
        self.writeVint(11)
        self.writeVint(99999)  # mortis trophies for rank
        self.writeVint(16)
        self.writeVint(12)
        self.writeVint(99999)  # crow trophies for rank
        self.writeVint(16)
        self.writeVint(13)
        self.writeVint(99999)  # poco trophies for rank
        self.writeVint(16)
        self.writeVint(14)
        self.writeVint(99999)  # bo trophies for rank
        self.writeVint(16)
        self.writeVint(15)
        self.writeVint(99999)  # piper trophies for rank
        self.writeVint(16)
        self.writeVint(16)
        self.writeVint(99999)  # pam trophies for rank
        self.writeVint(16)
        self.writeVint(17)
        self.writeVint(99999)  # tara trophies for rank
        self.writeVint(16)
        self.writeVint(18)
        self.writeVint(99999)  # darryl trophies for rank
        self.writeVint(16)
        self.writeVint(19)
        self.writeVint(99999)  # penny trophies for rank
        self.writeVint(16)
        self.writeVint(20)
        self.writeVint(99999)  # frank trophies for rank
        self.writeVint(16)
        self.writeVint(21)
        self.writeVint(99999)  # gene trophies for rank
        self.writeVint(16)
        self.writeVint(22)
        self.writeVint(99999)  # tick trophies for rank
        self.writeVint(16)
        self.writeVint(23)
        self.writeVint(99999)  # leon trophies for rank
        self.writeVint(16)
        self.writeVint(24)
        self.writeVint(99999)  # rosa trophies for rank
        self.writeVint(16)
        self.writeVint(25)
        self.writeVint(99999)  # carl trophies for rank
        self.writeVint(16)
        self.writeVint(26)
        self.writeVint(99999)  # bibi trophies for rank
        self.writeVint(16)
        self.writeVint(27)
        self.writeVint(99999)  # 8bit trophies for rank
        self.writeVint(16)
        self.writeVint(28)
        self.writeVint(99999)  # sandy trophies for rank
        self.writeVint(16)
        self.writeVint(29)
        self.writeVint(99999)  # bea trophies for rank
        self.writeVint(16)
        self.writeVint(30)
        self.writeVint(99999)  # emz trophies for rank
        self.writeVint(16)
        self.writeVint(31)
        self.writeVint(99999)  # mr p trophies for rank
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

        self.writeVint(35)  # brawlers count

        self.writeVint(16)
        self.writeVint(0)
        self.writeVint(1440)  # hmm what could this be?
        self.writeVint(16)
        self.writeVint(1)
        self.writeVint(1440)
        self.writeVint(16)
        self.writeVint(2)
        self.writeVint(1440)
        self.writeVint(16)
        self.writeVint(3)
        self.writeVint(1440)
        self.writeVint(16)
        self.writeVint(4)
        self.writeVint(1440)
        self.writeVint(16)
        self.writeVint(5)
        self.writeVint(1440)
        self.writeVint(16)
        self.writeVint(6)
        self.writeVint(1440)
        self.writeVint(16)
        self.writeVint(7)
        self.writeVint(1440)
        self.writeVint(16)
        self.writeVint(8)
        self.writeVint(1440)
        self.writeVint(16)
        self.writeVint(9)
        self.writeVint(1440)
        self.writeVint(16)
        self.writeVint(10)
        self.writeVint(1440)
        self.writeVint(16)
        self.writeVint(11)
        self.writeVint(1440)
        self.writeVint(16)
        self.writeVint(12)
        self.writeVint(1440)
        self.writeVint(16)
        self.writeVint(13)
        self.writeVint(1440)
        self.writeVint(16)
        self.writeVint(14)
        self.writeVint(1440)
        self.writeVint(16)
        self.writeVint(15)
        self.writeVint(1440)
        self.writeVint(16)
        self.writeVint(16)
        self.writeVint(1440)
        self.writeVint(16)
        self.writeVint(17)
        self.writeVint(1440)
        self.writeVint(16)
        self.writeVint(18)
        self.writeVint(1440)
        self.writeVint(16)
        self.writeVint(19)
        self.writeVint(1440)
        self.writeVint(16)
        self.writeVint(20)
        self.writeVint(1440)
        self.writeVint(16)
        self.writeVint(21)
        self.writeVint(1440)
        self.writeVint(16)
        self.writeVint(22)
        self.writeVint(1440)
        self.writeVint(16)
        self.writeVint(23)
        self.writeVint(1440)
        self.writeVint(16)
        self.writeVint(24)
        self.writeVint(1440)
        self.writeVint(16)
        self.writeVint(25)
        self.writeVint(1440)
        self.writeVint(16)
        self.writeVint(26)
        self.writeVint(1440)
        self.writeVint(16)
        self.writeVint(27)
        self.writeVint(1440)
        self.writeVint(16)
        self.writeVint(28)
        self.writeVint(1440)
        self.writeVint(16)
        self.writeVint(29)
        self.writeVint(1440)
        self.writeVint(16)
        self.writeVint(30)
        self.writeVint(1440)
        self.writeVint(16)
        self.writeVint(31)
        self.writeVint(1440)
        self.writeVint(16)
        self.writeVint(32)
        self.writeVint(1440)
        self.writeVint(16)
        self.writeVint(34)
        self.writeVint(1440)
        self.writeVint(16)
        self.writeVint(37)
        self.writeVint(1440)

        self.writeVint(35)  # brawlers count

        self.writeVint(16)
        self.writeVint(0)
        self.writeVint(8)  # shelly power level (value shows in game +1, so value 8 = power 9)
        self.writeVint(16)
        self.writeVint(1)
        self.writeVint(8)  # colt power level
        self.writeVint(16)
        self.writeVint(2)
        self.writeVint(8)  # bull power level
        self.writeVint(16)
        self.writeVint(3)
        self.writeVint(8)  # brock power level
        self.writeVint(16)
        self.writeVint(4)
        self.writeVint(8)  # rico power level
        self.writeVint(16)
        self.writeVint(5)
        self.writeVint(8)  # spike power level
        self.writeVint(16)
        self.writeVint(6)
        self.writeVint(8)  # barley power level
        self.writeVint(16)
        self.writeVint(7)
        self.writeVint(8)  # jessie power level
        self.writeVint(16)
        self.writeVint(8)
        self.writeVint(8)  # nita power level
        self.writeVint(16)
        self.writeVint(9)
        self.writeVint(8)  # dynamike power level
        self.writeVint(16)
        self.writeVint(10)
        self.writeVint(8)  # primo power level
        self.writeVint(16)
        self.writeVint(11)
        self.writeVint(8)  # mortis power level
        self.writeVint(16)
        self.writeVint(12)
        self.writeVint(8)  # crow power level
        self.writeVint(16)
        self.writeVint(13)
        self.writeVint(8)  # poco power level
        self.writeVint(16)
        self.writeVint(14)
        self.writeVint(8)  # bo power level
        self.writeVint(16)
        self.writeVint(15)
        self.writeVint(8)  # piper power level
        self.writeVint(16)
        self.writeVint(16)
        self.writeVint(8)  # pam power level
        self.writeVint(16)
        self.writeVint(17)
        self.writeVint(8)  # tara power level
        self.writeVint(16)
        self.writeVint(18)
        self.writeVint(8)  # darryl power level
        self.writeVint(16)
        self.writeVint(19)
        self.writeVint(8)  # peny power level
        self.writeVint(16)
        self.writeVint(20)
        self.writeVint(8)  # frank power level
        self.writeVint(16)
        self.writeVint(21)
        self.writeVint(8)  # gene power level
        self.writeVint(16)
        self.writeVint(22)
        self.writeVint(8)  # tick power level
        self.writeVint(16)
        self.writeVint(23)
        self.writeVint(8)  # leon power level
        self.writeVint(16)
        self.writeVint(24)
        self.writeVint(8)  # rosa power level
        self.writeVint(16)
        self.writeVint(25)
        self.writeVint(8)  # carl power level
        self.writeVint(16)
        self.writeVint(26)
        self.writeVint(8)  # bibi power level
        self.writeVint(16)
        self.writeVint(27)
        self.writeVint(8)  # 8bit power level
        self.writeVint(16)
        self.writeVint(28)
        self.writeVint(8)  # sandy power level
        self.writeVint(16)
        self.writeVint(29)
        self.writeVint(8)  # bea power level
        self.writeVint(16)
        self.writeVint(30)
        self.writeVint(8)  # emz power level
        self.writeVint(16)
        self.writeVint(31)
        self.writeVint(8)  # mr p  power level
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
        self.writeVint(23)
        self.writeVint(76)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(77)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(78)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(79)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(80)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(81)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(82)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(83)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(84)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(85)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(86)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(87)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(88)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(89)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(90)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(91)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(92)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(93)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(94)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(99)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(104)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(109)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(114)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(119)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(124)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(129)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(134)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(135)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(136)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(137)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(138)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(139)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(140)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(141)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(142)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(143)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(144)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(145)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(146)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(147)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(148)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(149)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(150)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(151)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(152)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(153)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(154)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(155)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(156)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(157)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(158)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(159)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(160)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(161)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(162)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(163)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(164)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(165)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(166)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(167)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(168)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(169)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(170)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(172)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(174)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(175)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(176)
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
        self.writeVint(23)
        self.writeVint(222)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(223)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(240)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(241)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(242)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(243)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(244)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(245)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(246)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(247)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(248)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(249)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(250)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(251)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(252)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(253)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(254)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(255)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(256)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(257)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(258)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(259)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(260)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(261)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(262)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(263)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(264)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(265)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(266)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(267)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(268)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(269)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(270)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(271)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(272)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(273)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(274)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(275)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(276)
        self.writeVint(1)

        self.writeVint(35)  # brawlers count

        self.writeVint(16)
        self.writeVint(0)
        self.writeVint(2)  # shelly "new" tag
        self.writeVint(16)
        self.writeVint(1)
        self.writeVint(2)  # colt "new" tag
        self.writeVint(16)
        self.writeVint(2)
        self.writeVint(2)  # bull "new" tag
        self.writeVint(16)
        self.writeVint(3)
        self.writeVint(2)  # brock "new" tag
        self.writeVint(16)
        self.writeVint(4)
        self.writeVint(2)  # rico "new" tag
        self.writeVint(16)
        self.writeVint(5)
        self.writeVint(2)  # spike "new" tag
        self.writeVint(16)
        self.writeVint(6)
        self.writeVint(2)  # barley "new" tag
        self.writeVint(16)
        self.writeVint(7)
        self.writeVint(2)  # jessie "new" tag
        self.writeVint(16)
        self.writeVint(2)
        self.writeVint(2)  # nita "new" tag
        self.writeVint(16)
        self.writeVint(9)
        self.writeVint(2)  # dynamike "new" tag
        self.writeVint(16)
        self.writeVint(10)
        self.writeVint(2)  # primo "new" tag
        self.writeVint(16)
        self.writeVint(11)
        self.writeVint(2)  # mortis "new" tag
        self.writeVint(16)
        self.writeVint(12)
        self.writeVint(2)  # crow "new" tag
        self.writeVint(16)
        self.writeVint(13)
        self.writeVint(2)  # poco "new" tag
        self.writeVint(16)
        self.writeVint(14)
        self.writeVint(2)  # bo "new" tag
        self.writeVint(16)
        self.writeVint(15)
        self.writeVint(2)  # piper "new" tag
        self.writeVint(16)
        self.writeVint(16)
        self.writeVint(2)  # pam "new" tag
        self.writeVint(16)
        self.writeVint(17)
        self.writeVint(2)  # tara "new" tag
        self.writeVint(16)
        self.writeVint(12)
        self.writeVint(2)  # darryl "new" tag
        self.writeVint(16)
        self.writeVint(19)
        self.writeVint(2)  # peny "new" tag
        self.writeVint(16)
        self.writeVint(20)
        self.writeVint(2)  # frank "new" tag
        self.writeVint(16)
        self.writeVint(21)
        self.writeVint(2)  # gene "new" tag
        self.writeVint(16)
        self.writeVint(22)
        self.writeVint(2)  # tick "new" tag
        self.writeVint(16)
        self.writeVint(23)
        self.writeVint(2)  # leon "new" tag
        self.writeVint(16)
        self.writeVint(24)
        self.writeVint(2)  # rosa "new" tag
        self.writeVint(16)
        self.writeVint(25)
        self.writeVint(2)  # carl "new" tag
        self.writeVint(16)
        self.writeVint(26)
        self.writeVint(2)  # bibi "new" tag
        self.writeVint(16)
        self.writeVint(27)
        self.writeVint(2)  # 8bit "new" tag
        self.writeVint(16)
        self.writeVint(22)
        self.writeVint(2)  # sandy "new" tag
        self.writeVint(16)
        self.writeVint(29)
        self.writeVint(2)  # bea "new" tag
        self.writeVint(16)
        self.writeVint(30)
        self.writeVint(2)  # emz "new" tag
        self.writeVint(16)
        self.writeVint(31)
        self.writeVint(2)  # mr p  "new" tag
        self.writeVint(16)
        self.writeVint(32)
        self.writeVint(2)  # max "new" tag
        self.writeVint(16)
        self.writeVint(34)
        self.writeVint(2)  # jacky "new" tag
        self.writeVint(16)
        self.writeVint(37)

        self.writeVint(2)

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



