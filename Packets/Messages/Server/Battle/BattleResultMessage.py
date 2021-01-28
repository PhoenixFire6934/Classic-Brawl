from Utils.Writer import Writer
from Database.DataBase import DataBase

class BattleResultMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 23456
        self.player = player

    def encode(self):
        self.writeVint(2)

        self.writeVint(self.player.rank) # player rank

        brawler_trophies = self.player.brawlers_trophies[str(self.player.brawler_id)]


        if 0 <= brawler_trophies <= 49:
            rank_1_val = 10
            rank_2_val = 8
            rank_3_val = 7
            rank_4_val = 6
            rank_5_val = 4
            rank_6_val = 2
            rank_7_val = 2
            rank_8_val = 1
            rank_9_val = 0
            rank_10_val = 0
        else:
            if 50 <= brawler_trophies <= 99:
                rank_1_val = 10
                rank_2_val = 8
                rank_3_val = 7
                rank_4_val = 6
                rank_5_val = 3
                rank_6_val = 2
                rank_7_val = 2
                rank_8_val = 0
                rank_9_val = -1
                rank_10_val = -2

            if 100 <= brawler_trophies <= 199:
                rank_1_val = 10
                rank_2_val = 8
                rank_3_val = 7
                rank_4_val = 6
                rank_5_val = 3
                rank_6_val = 1
                rank_7_val = 0
                rank_8_val = -1
                rank_9_val = -2
                rank_10_val = -2

            if 200 <= brawler_trophies <= 299:
                rank_1_val = 10
                rank_2_val = 8
                rank_3_val = 6
                rank_4_val = 5
                rank_5_val = 3
                rank_6_val = 1
                rank_7_val = 0
                rank_8_val = -2
                rank_9_val = -3
                rank_10_val = -3

            if 300 <= brawler_trophies <= 399:
                rank_1_val = 10
                rank_2_val = 8
                rank_3_val = 6
                rank_4_val = 5
                rank_5_val = 2
                rank_6_val = 0
                rank_7_val = 0
                rank_8_val = -3
                rank_9_val = -4
                rank_10_val = -4

            if 400 <= brawler_trophies <= 499:
                rank_1_val = 10
                rank_2_val = 8
                rank_3_val = 6
                rank_4_val = 5
                rank_5_val = 2
                rank_6_val = -1
                rank_7_val = -2
                rank_8_val = -3
                rank_9_val = -5
                rank_10_val = -5

            if 500 <= brawler_trophies <= 599:
                rank_1_val = 10
                rank_2_val = 8
                rank_3_val = 6
                rank_4_val = 4
                rank_5_val = 2
                rank_6_val = -1
                rank_7_val = -2
                rank_8_val = -5
                rank_9_val = -6
                rank_10_val = -6

            if 600 <= brawler_trophies <= 699:
                rank_1_val = 10
                rank_2_val = 8
                rank_3_val = 6
                rank_4_val = 4
                rank_5_val = 1
                rank_6_val = -2
                rank_7_val = -2
                rank_8_val = -5
                rank_9_val = -7
                rank_10_val = -8

            if 700 <= brawler_trophies <= 799:
                rank_1_val = 10
                rank_2_val = 8
                rank_3_val = 6
                rank_4_val = 4
                rank_5_val = 1
                rank_6_val = -3
                rank_7_val = -4
                rank_8_val = -5
                rank_9_val = -8
                rank_10_val = -9

            if 800 <= brawler_trophies <= 899:
                rank_1_val = 9
                rank_2_val = 7
                rank_3_val = 5
                rank_4_val = 2
                rank_5_val = 0
                rank_6_val = -3
                rank_7_val = -4
                rank_8_val = -7
                rank_9_val = -9
                rank_10_val = -10

            if 900 <= brawler_trophies <= 999:
                rank_1_val = 8
                rank_2_val = 6
                rank_3_val = 4
                rank_4_val = 1
                rank_5_val = -1
                rank_6_val = -3
                rank_7_val = -6
                rank_8_val = -8
                rank_9_val = -10
                rank_10_val = -11

            if 1000 <= brawler_trophies <= 1099:
                rank_1_val = 6
                rank_2_val = 5
                rank_3_val = 3
                rank_4_val = 1
                rank_5_val = -2
                rank_6_val = -5
                rank_7_val = -6
                rank_8_val = -9
                rank_9_val = -11
                rank_10_val = -12

            if 1100 <= brawler_trophies <= 1199:
                rank_1_val = 5
                rank_2_val = 4
                rank_3_val = 1
                rank_4_val = 0
                rank_5_val = -2
                rank_6_val = -6
                rank_7_val = -7
                rank_8_val = -10
                rank_9_val = -12
                rank_10_val = -13

            if brawler_trophies >= 1200:
                rank_1_val = 5
                rank_2_val = 3
                rank_3_val = 0
                rank_4_val = -1
                rank_5_val = -2
                rank_6_val = -6
                rank_7_val = -8
                rank_8_val = -11
                rank_9_val = -12
                rank_10_val = -13


        if self.player.rank == 1:
            new_trophies = self.player.trophies + rank_1_val
            self.player.brawlers_trophies[str(self.player.brawler_id)] = brawler_trophies + rank_1_val
            DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
            DataBase.replaceValue(self, 'trophies', new_trophies)

        elif self.player.rank == 2:
            new_trophies = self.player.trophies + rank_2_val
            self.player.brawlers_trophies[str(self.player.brawler_id)] = brawler_trophies + rank_2_val
            DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
            DataBase.replaceValue(self, 'trophies', new_trophies)

        elif self.player.rank == 3:
            new_trophies = self.player.trophies + rank_3_val
            self.player.brawlers_trophies[str(self.player.brawler_id)] = brawler_trophies + rank_3_val
            DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
            DataBase.replaceValue(self, 'trophies', new_trophies)

        elif self.player.rank == 4:
            new_trophies = self.player.trophies + rank_4_val
            self.player.brawlers_trophies[str(self.player.brawler_id)] = brawler_trophies + rank_4_val
            DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
            DataBase.replaceValue(self, 'trophies', new_trophies)

        elif self.player.rank == 5:
            new_trophies = self.player.trophies + rank_5_val
            self.player.brawlers_trophies[str(self.player.brawler_id)] = brawler_trophies + rank_5_val
            DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
            DataBase.replaceValue(self, 'trophies', new_trophies)

        elif self.player.rank == 6:
            new_trophies = self.player.trophies + rank_6_val
            self.player.brawlers_trophies[str(self.player.brawler_id)] = brawler_trophies + rank_6_val
            DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
            DataBase.replaceValue(self, 'trophies', new_trophies)

        elif self.player.rank == 7:
            new_trophies = self.player.trophies + rank_7_val
            self.player.brawlers_trophies[str(self.player.brawler_id)] = brawler_trophies + rank_7_val
            DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
            DataBase.replaceValue(self, 'trophies', new_trophies)

        elif self.player.rank == 8:
            new_trophies = self.player.trophies + rank_8_val
            self.player.brawlers_trophies[str(self.player.brawler_id)] = brawler_trophies + rank_8_val
            DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
            DataBase.replaceValue(self, 'trophies', new_trophies)

        elif self.player.rank == 9:
            new_trophies = self.player.trophies + rank_9_val
            self.player.brawlers_trophies[str(self.player.brawler_id)] = brawler_trophies + rank_9_val
            DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
            DataBase.replaceValue(self, 'trophies', new_trophies)

        elif self.player.rank == 10:
            new_trophies = self.player.trophies + rank_10_val
            self.player.brawlers_trophies[str(self.player.brawler_id)] = brawler_trophies + rank_10_val
            DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
            DataBase.replaceValue(self, 'trophies', new_trophies)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(32)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(10)
        self.writeVint(1)
        self.writeVint(16)
        self.writeVint(self.player.brawler_id)
        self.writeVint(29)
        self.writeVint(self.player.skin_id)
        self.writeVint(99999)
        self.writeVint(0)
        self.writeVint(10)
        self.writeVint(0)
        self.writeString(self.player.name)
        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)
        self.writeVint(2)
        self.writeVint(16)
        self.writeVint(11)
        self.writeVint(0)
        self.writeVint(99999)
        self.writeVint(0)
        self.writeVint(10)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(1)
        self.writeVint(49)
        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)
        self.writeVint(2)
        self.writeVint(16)
        self.writeVint(35)
        self.writeVint(0)
        self.writeVint(99999)
        self.writeVint(0)
        self.writeVint(10)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(1)
        self.writeVint(50)
        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)
        self.writeVint(2)
        self.writeVint(16)
        self.writeVint(31)
        self.writeVint(0)
        self.writeVint(99999)
        self.writeVint(0)
        self.writeVint(10)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(1)
        self.writeVint(51)
        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)
        self.writeVint(2)
        self.writeVint(16)
        self.writeVint(3)
        self.writeVint(0)
        self.writeVint(99999)
        self.writeVint(0)
        self.writeVint(10)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(1)
        self.writeVint(52)
        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)
        self.writeVint(2)
        self.writeVint(16)
        self.writeVint(26)
        self.writeVint(0)
        self.writeVint(99999)
        self.writeVint(0)
        self.writeVint(10)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(1)
        self.writeVint(53)
        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)
        self.writeVint(2)
        self.writeVint(16)
        self.writeVint(34)
        self.writeVint(0)
        self.writeVint(99999)
        self.writeVint(0)
        self.writeVint(10)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(1)
        self.writeVint(54)
        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)
        self.writeVint(2)
        self.writeVint(16)
        self.writeVint(25)
        self.writeVint(0)
        self.writeVint(99999)
        self.writeVint(0)
        self.writeVint(10)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(1)
        self.writeVint(55)
        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)
        self.writeVint(2)
        self.writeVint(16)
        self.writeVint(8)
        self.writeVint(0)
        self.writeVint(99999)
        self.writeVint(0)
        self.writeVint(10)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(1)
        self.writeVint(56)
        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)
        self.writeVint(2)
        self.writeVint(16)
        self.writeVint(30)
        self.writeVint(0)
        self.writeVint(99999)
        self.writeVint(0)
        self.writeVint(10)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(1)
        self.writeVint(57)
        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(28)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(-1040385)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
