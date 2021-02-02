from Utils.Writer import Writer
from Database.DatabaseManager import DataBase


class BattleResult2Message(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 23456
        self.player = player

    def encode(self):
        self.writeVint(0)
        self.writeVint(self.player.battle_result)

        brawler_trophies = self.player.brawlers_trophies[str(self.player.brawler_id)]
        brawler_trophies_for_rank = self.player.brawlers_trophies_in_rank[str(self.player.brawler_id)]
        exp_reward = [8, 6, 4]
        player_tokens_reward = [20, 15, 10]

        if 0 <= brawler_trophies <= 49:
            win_val = 8
            lose_val = 0

        else:
            if 50 <= brawler_trophies <= 99:
                win_val = 8
                lose_val = -1

            if 100 <= brawler_trophies <= 199:
                win_val = 8
                lose_val = -2

            if 200 <= brawler_trophies <= 299:
                win_val = 8
                lose_val = -3

            if 300 <= brawler_trophies <= 399:
                win_val = 8
                lose_val = -4

            if 400 <= brawler_trophies <= 499:
                win_val = 8
                lose_val = -5

            if 500 <= brawler_trophies <= 599:
                win_val = 8
                lose_val = -6

            if 600 <= brawler_trophies <= 699:
                win_val = 8
                lose_val = -7

            if 700 <= brawler_trophies <= 799:
                win_val = 8
                lose_val = -8

            if 800 <= brawler_trophies <= 899:
                win_val = 7
                lose_val = -9

            if 900 <= brawler_trophies <= 999:
                win_val = 6
                lose_val = -10

            if 1000 <= brawler_trophies <= 1099:
                win_val = 5
                lose_val = -11

            if 1100 <= brawler_trophies <= 1199:
                win_val = 4
                lose_val = -12

            if brawler_trophies >= 1200:
                win_val = 3
                lose_val = -12

        if self.player.battle_result == 0:
            self.player.ThreeVSThree_wins += 1
            self.player.player_experience += exp_reward[0]
            if self.player.tokensdoubler > 0:
                if self.player.tokensdoubler <= player_tokens_reward[0]:
                     print("OLD", player_tokens_reward[0])
                     player_tokens_reward[0] += self.player.tokensdoubler
                     self.player.tokensdoubler = 0
                     self.player.brawl_boxes += player_tokens_reward[0]
                     DataBase.replaceValue(self, "tokensdoubler", self.player.tokensdoubler)
                     DataBase.replaceValue(self, "brawlBoxes", self.player.brawl_boxes)
                     print("NEW", player_tokens_reward[0])
                else:
                    print("OLD", player_tokens_reward[0])
                    self.player.tokensdoubler -= player_tokens_reward[0]
                    player_tokens_reward[0] += player_tokens_reward[0]
                    self.player.brawl_boxes += player_tokens_reward[0]
                    DataBase.replaceValue(self, "tokensdoubler", self.player.tokensdoubler)
                    DataBase.replaceValue(self, "brawlBoxes", self.player.brawl_boxes)
                    print("NEW", player_tokens_reward[0])
            else:
                print("OLD", player_tokens_reward[0])
                self.player.brawl_boxes += player_tokens_reward[0]
                print("NEW", player_tokens_reward[0])
            self.player.trophies += win_val
            self.player.brawlers_trophies[str(self.player.brawler_id)] = brawler_trophies + win_val
            if self.player.brawlers_trophies_in_rank[str(self.player.brawler_id)] < self.player.brawlers_trophies[str(self.player.brawler_id)]:
                self.player.brawlers_trophies_in_rank[str(self.player.brawler_id)] = brawler_trophies_for_rank + win_val

            DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
            DataBase.replaceValue(self, 'brawlersTrophiesForRank', self.player.brawlers_trophies_in_rank)
            DataBase.replaceValue(self, 'trophies', self.player.trophies)
            DataBase.replaceValue(self, '3vs3Wins', self.player.ThreeVSThree_wins)
            DataBase.replaceValue(self, 'playerExp', self.player.player_experience)
        else:
            self.player.player_experience += exp_reward[2]
            if self.player.tokensdoubler > 0:
                if self.player.tokensdoubler <= player_tokens_reward[2]:
                     print("OLD", player_tokens_reward[2])
                     player_tokens_reward[2] += self.player.tokensdoubler
                     self.player.tokensdoubler = 0
                     self.player.brawl_boxes += player_tokens_reward[2]
                     DataBase.replaceValue(self, "tokensdoubler", self.player.tokensdoubler)
                     DataBase.replaceValue(self, "brawlBoxes", self.player.brawl_boxes)
                     print("NEW", player_tokens_reward[2])
                else:
                    print("OLD", player_tokens_reward[2])
                    self.player.tokensdoubler -= player_tokens_reward[2]
                    player_tokens_reward[2] += player_tokens_reward[2]
                    self.player.brawl_boxes += player_tokens_reward[2]
                    DataBase.replaceValue(self, "tokensdoubler", self.player.tokensdoubler)
                    DataBase.replaceValue(self, "brawlBoxes", self.player.brawl_boxes)
                    print("NEW", player_tokens_reward[2])
            else:
                print("OLD", player_tokens_reward[2])
                self.player.brawl_boxes += player_tokens_reward[2]
                print("NEW", player_tokens_reward[2])
            self.player.trophies -= lose_val
            self.player.brawlers_trophies[str(self.player.brawler_id)] = brawler_trophies + lose_val

            DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
            DataBase.replaceValue(self, 'brawlersTrophiesForRank', self.player.brawlers_trophies_in_rank)
            DataBase.replaceValue(self, 'trophies', self.player.trophies)
            DataBase.replaceValue(self, 'playerExp', self.player.player_experience)

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
        self.writeVint(6)
        self.writeVint(5)
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

        self.writeVint(0)
        self.writeVint(16)
        self.writeVint(self.player.bot1)
        self.writeVint(0)
        self.writeVint(99999)
        self.writeVint(0)
        self.writeVint(10)
        self.writeVint(0)
        self.writeString(self.player.bot1_n)
        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)

        self.writeVint(0)
        self.writeVint(16)
        self.writeVint(self.player.bot2)
        self.writeVint(0)
        self.writeVint(99999)
        self.writeVint(0)
        self.writeVint(10)
        self.writeVint(0)
        self.writeString(self.player.bot2_n)
        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)

        self.writeVint(2)
        self.writeVint(16)
        self.writeVint(self.player.bot3)
        self.writeVint(0)
        self.writeVint(99999)
        self.writeVint(0)
        self.writeVint(10)
        self.writeVint(0)
        self.writeString(self.player.bot3_n)
        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)

        self.writeVint(2)
        self.writeVint(16)
        self.writeVint(self.player.bot4)
        self.writeVint(0)
        self.writeVint(99999)
        self.writeVint(0)
        self.writeVint(10)
        self.writeVint(0)
        self.writeString(self.player.bot4_n)
        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)

        self.writeVint(2)
        self.writeVint(16)
        self.writeVint(self.player.bot5)
        self.writeVint(0)
        self.writeVint(99999)
        self.writeVint(0)
        self.writeVint(10)
        self.writeVint(0)
        self.writeString(self.player.bot5_n)
        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)