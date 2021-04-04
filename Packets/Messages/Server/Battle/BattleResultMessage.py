from Utils.Writer import Writer
from Database.DatabaseManager import DataBase


class BattleResultMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 23456
        self.player = player

    def encode(self):
        self.writeVint(0)
        self.writeVint(self.player.battle_result)

        brawler_trophies = self.player.brawlers_trophies[str(self.player.brawler_id)]
        brawler_trophies_for_rank = self.player.brawlers_trophies_in_rank[str(self.player.brawler_id)]
        if self.player.Brawler_starPower[str(self.player.brawler_id)] >= 1:
            brawler_level = self.player.Brawler_level[str(self.player.brawler_id)] + 2
        else:
            brawler_level = self.player.Brawler_level[str(self.player.brawler_id)] + 1
        exp_reward = [8, 6, 4]
        token_list = [20,15,10]
        practice_exp_reward = [4, 3, 2] 
        practice_token_list = [10,8,5]
        mvp_exp_reward = [10, 5]
        
        
        if self.player.battle_result == 0:
            if self.player.battle_tokens <= 0 and self.player.collected_experience >= 1000:
                result = self.player.result + 7
            elif self.player.battle_tokens <= 0:
                result = self.player.result + 5
            elif self.player.collected_experience >= 1000:
                result = self.player.result + 3
            else:
                result = self.player.result + 1
            starplayer = 5
        if self.player.battle_result == 1:
            if self.player.battle_tokens <= 0 and self.player.collected_experience >= 1000:
                result = self.player.result + 6
            elif self.player.battle_tokens <= 0:
                result = self.player.result + 4
            elif self.player.collected_experience >= 1000:
                result = self.player.result + 2
            else:
                result = self.player.result
            starplayer = 1
        if self.player.battle_result == 2:
            if self.player.battle_tokens <= 0 and self.player.collected_experience >= 1000:
                result = self.player.result + 6
            elif self.player.battle_tokens <= 0:
                result = self.player.result + 4
            elif self.player.collected_experience >= 1000:
                result = self.player.result + 2
            else:
                result = self.player.result
            starplayer = 5
            
        if starplayer == 5:
            starplayerexperience = mvp_exp_reward[0]
            practice_starplayerexperience = mvp_exp_reward[1]
        else:
            starplayerexperience = 0
            practice_starplayerexperience = 0
                    

        if 0 <= brawler_trophies <= 29:
            win_val = 6
            lose_val = 0
            lose_val2 = 0

        else:
            if 30 <= brawler_trophies <= 59:
                win_val = 6
                lose_val = -1
                lose_val2 = -64

            if 60 <= brawler_trophies <= 99:
                win_val = 6
                lose_val = -2
                lose_val2 = -63

            if 100 <= brawler_trophies <= 139:
                win_val = 5
                lose_val = -2
                lose_val2 = -63

            if 140 <= brawler_trophies <= 219:
                win_val = 5
                lose_val = -3
                lose_val2 = -62

            if 220 <= brawler_trophies <= 299:
                win_val = 5
                lose_val = -4
                lose_val2 = -61

            if 300 <= brawler_trophies <= 499:
                win_val = 5
                lose_val = -5
                lose_val2 = -60

            if 500 <= brawler_trophies <= 599:
                win_val = 5
                lose_val = -6
                lose_val2 = -59

            if 600 <= brawler_trophies <= 699:
                win_val = 4
                lose_val = -6
                lose_val2 = -59

            if 700 <= brawler_trophies <= 799:
                win_val = 3
                lose_val = -6
                lose_val2 = -59

            if 800 <= brawler_trophies <= 899:
                win_val = 3
                lose_val = -7
                lose_val2 = -58

            if brawler_trophies >= 900:
                win_val = 2
                lose_val = -7
                lose_val2 = -58

        if self.player.battle_result == 0:
            trophiesinresult = win_val
            if result in [0, 1, 2, 3, 8, 9, 10, 11]:
                tokens = practice_token_list[0]
            if result in [4, 5, 6, 7, 12, 13, 14, 15]:
                tokens = 0
            if result in [0, 1, 4, 5, 8, 9, 12, 13]:
                mvpexperience = practice_starplayerexperience
                experience = practice_exp_reward[0]
            if result in [2, 3, 6, 7, 10, 11, 14, 15]:
                mvpexperience = 0
                experience = 0
            if result in [1, 3, 5, 7, 9, 11, 13, 15]:
                startoken = 1
            if result in [0, 2, 4, 6, 8, 10, 12, 14]:
                startoken = 0
            if 0 <= result <= 15:
                trophies = 0
                
            if result in [16, 17, 18, 19, 24, 25, 26, 27]:
                tokens = token_list[0]
            if result in [20, 21, 22, 23, 28, 29, 30, 31]:
                tokens = 0
            if result in [16, 17, 20, 21, 24, 25, 28, 29]:
                mvpexperience = starplayerexperience
                experience = exp_reward[0]
            if result in [18, 19, 22, 23, 26, 27, 30, 31]:
                mvpexperience = 0
                experience = 0
            if result in [17, 19, 21, 23, 25, 27, 29, 31]:
                startoken = 1
            if result in [16, 18, 20, 22, 24, 26, 28, 30]:
                startoken = 0
            if 16 <= result <= 31:
                trophies = win_val
            
                
            self.player.ThreeVSThree_wins += 1
            self.player.player_experience += experience + mvpexperience
            self.player.collected_experience += experience + mvpexperience
            if self.player.battle_tokens <= 0:
                token = 0
            if self.player.battle_tokens > tokens:
                token = tokens
            if tokens > self.player.battle_tokens: 
                token = self.player.battle_tokens
            if self.player.tokensdoubler <= 0:
                doubledtokens = 0
            if self.player.tokensdoubler > token:
                doubledtokens = token
            if token > self.player.tokensdoubler: 
                doubledtokens = self.player.tokensdoubler
            battle_tokens = self.player.battle_tokens - token
            remainingtokens = (self.player.tokensdoubler) - doubledtokens
            totaltokens = token + doubledtokens
            new_trophies = self.player.trophies + trophies
            new_tokens = self.player.brawl_boxes + totaltokens
            new_startokens = self.player.big_boxes + startoken
            self.player.brawlers_trophies[str(self.player.brawler_id)] = brawler_trophies + trophies
            if self.player.brawlers_trophies_in_rank[str(self.player.brawler_id)] < self.player.brawlers_trophies[str(self.player.brawler_id)]:
                self.player.brawlers_trophies_in_rank[str(self.player.brawler_id)] = brawler_trophies_for_rank + trophies
            DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
            DataBase.replaceValue(self, 'brawlersTrophiesForRank', self.player.brawlers_trophies_in_rank)
            DataBase.replaceValue(self, 'brawlersTrophiesForRank', self.player.brawlers_trophies_in_rank)
            DataBase.replaceValue(self, 'trophies', new_trophies)
            DataBase.replaceValue(self, 'brawlBoxes', new_tokens)
            DataBase.replaceValue(self, 'bigBoxes', new_startokens)
            DataBase.replaceValue(self, 'availableTokens', battle_tokens)
            DataBase.replaceValue(self, 'tokensdoubler', remainingtokens)
            DataBase.replaceValue(self, 'playerExp', self.player.player_experience)
            DataBase.replaceValue(self, 'cappedExp', self.player.collected_experience)
            DataBase.replaceValue(self, '3vs3Wins', self.player.ThreeVSThree_wins)
            
        elif self.player.battle_result == 1:
            trophiesinresult = lose_val2
            if result in [0, 1, 2, 3, 8, 9, 10, 11]:
                tokens = practice_token_list[2]
            if result in [4, 5, 6, 7, 12, 13, 14, 15]:
                tokens = 0
            if result in [0, 1, 4, 5, 8, 9, 12, 13]:
                mvpexperience = 0
                experience = practice_exp_reward[2]
            if result in [2, 3, 6, 7, 10, 11, 14, 15]:
                mvpexperience = 0
                experience = 0
            if 0 <= result <= 15:
                trophies = 0
                startoken = 0
                
            if result in [16, 17, 18, 19, 24, 25, 26, 27]:
                tokens = token_list[2]
            if result in [20, 21, 22, 23, 28, 29, 30, 31]:
                tokens = 0
            if result in [16, 17, 20, 21, 24, 25, 28, 29]:
                mvpexperience = 0
                experience = exp_reward[2]
            if result in [18, 19, 22, 23, 26, 27, 30, 31]:
                mvpexperience = 0
                experience = 0
            if 16 <= result <= 31:
                trophies = lose_val
                startoken = 0
                
            self.player.player_experience += experience + mvpexperience
            self.player.collected_experience += experience + mvpexperience
            if self.player.battle_tokens <= 0:
                token = 0
            if self.player.battle_tokens > tokens:
                token = tokens
            if tokens > self.player.battle_tokens: 
                token = self.player.battle_tokens
            if self.player.tokensdoubler <= 0:
                doubledtokens = 0
            if self.player.tokensdoubler > token:
                doubledtokens = token
            if token > self.player.tokensdoubler: 
                doubledtokens = self.player.tokensdoubler
            battle_tokens = self.player.battle_tokens - token
            remainingtokens = (self.player.tokensdoubler) - doubledtokens
            totaltokens = token + doubledtokens
            new_trophies = self.player.trophies + trophies
            new_tokens = self.player.brawl_boxes + totaltokens
            self.player.brawlers_trophies[str(self.player.brawler_id)] = brawler_trophies + trophies
            DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
            DataBase.replaceValue(self, 'brawlersTrophiesForRank', self.player.brawlers_trophies_in_rank)
            DataBase.replaceValue(self, 'trophies', new_trophies)
            DataBase.replaceValue(self, 'brawlBoxes', new_tokens)
            DataBase.replaceValue(self, 'availableTokens', battle_tokens)
            DataBase.replaceValue(self, 'tokensdoubler', remainingtokens)
            DataBase.replaceValue(self, 'playerExp', self.player.player_experience)
            DataBase.replaceValue(self, 'cappedExp', self.player.collected_experience)

        elif self.player.battle_result == 2:
            trophiesinresult = 0
            if result in [0, 1, 2, 3, 8, 9, 10, 11]:
                tokens = practice_token_list[1]
            if result in [4, 5, 6, 7, 12, 13, 14, 15]:
                tokens = 0
            if result in [0, 1, 4, 5, 8, 9, 12, 13]:
                mvpexperience = practice_starplayerexperience
                experience = practice_exp_reward[1]
            if result in [2, 3, 6, 7, 10, 11, 14, 15]:
                mvpexperience = 0
                experience = 0
            if 0 <= result <= 15:
                trophies = 0
                startoken = 0
                
            if result in [16, 17, 18, 19, 24, 25, 26, 27]:
                tokens = token_list[1]
            if result in [20, 21, 22, 23, 28, 29, 30, 31]:
                tokens = 0
            if result in [16, 17, 20, 21, 24, 25, 28, 29]:
                mvpexperience = starplayerexperience
                experience = exp_reward[1]
            if result in [18, 19, 22, 23, 26, 27, 30, 31]:
                mvpexperience = 0
                experience = 0
            if 16 <= result <= 31:
                trophies = 0
                startoken = 0
                
            self.player.player_experience += experience + mvpexperience
            self.player.collected_experience += experience + mvpexperience
            if self.player.battle_tokens <= 0:
                token = 0
            if self.player.battle_tokens > tokens:
                token = tokens
            if tokens > self.player.battle_tokens: 
                token = self.player.battle_tokens
            if self.player.tokensdoubler <= 0:
                doubledtokens = 0
            if self.player.tokensdoubler > token:
                doubledtokens = token
            if token > self.player.tokensdoubler: 
                doubledtokens = self.player.tokensdoubler
            battle_tokens = self.player.battle_tokens - token
            remainingtokens = (self.player.tokensdoubler) - doubledtokens
            totaltokens = token + doubledtokens
            new_tokens = self.player.brawl_boxes + totaltokens
            DataBase.replaceValue(self, 'brawlBoxes', new_tokens)
            DataBase.replaceValue(self, 'availableTokens', battle_tokens)
            DataBase.replaceValue(self, 'tokensdoubler', remainingtokens)
            DataBase.replaceValue(self, 'playerExp', self.player.player_experience)
            DataBase.replaceValue(self, 'cappedExp', self.player.collected_experience)

        self.writeVint(token) # Tokens Gained
        if self.player.result < 16:
            self.writeVint(0) # Trophies Result 
        if self.player.result >= 16:
            self.writeVint(trophiesinresult) # Trophies Result
        self.writeVint(doubledtokens) # Doubled Tokens
        self.writeVint(remainingtokens) # Token Doubler Remaining
        self.writeVint(0) # Big Game/Robo Rumble Time
        self.writeVint(result) # Battle Result Info and Stuff
        self.writeVint(self.player.players) #Battle End Screen Players

        self.writeString(self.player.name) # Player Name
        self.writeVint(starplayer) # Self Star Player Type
        self.writeScId(16, self.player.brawler_id) # Player Brawler
        self.writeScId(29, self.player.skin_id) # Player Skin
        self.writeVint(brawler_trophies) # Brawler Trophies
        self.writeVint(brawler_level) # Brawler Power Level
        bool = True
        self.writeBoolean(bool)
        if bool == True:
            self.writeInt(self.player.high_id) # HighID
            self.writeInt(self.player.low_id) # LowID
        
        self.writeString(self.player.bot1_n) # Bot 1 Name
        self.writeVint(0) # Star Player Type
        self.writeScId(16, self.player.bot1) # Bot 1 Brawler
        self.writeVint(0) # Bot 1 Skin
        self.writeVint(0) # Brawler Trophies
        self.writeVint(1) # Brawler Power Level
        self.writeBoolean(False)
            
        self.writeString(self.player.bot2_n) # Bot 2 Name
        self.writeVint(0) # Star Player Type
        self.writeScId(16, self.player.bot2) # Bot 2 Brawler
        self.writeVint(0) # Bot 2 Skin
        self.writeVint(0) # Brawler Trophies
        self.writeVint(1) # Brawler Power Level
        self.writeBoolean(False)

        self.writeString(self.player.bot3_n) # Bot 3 Name
        self.writeVint(2) # Enemy Star Player Type
        self.writeScId(16, self.player.bot3) # Bot 3 Brawler
        self.writeVint(0) # Bot 3 Skin
        self.writeVint(0) # Brawler Trophies
        self.writeVint(1) # Brawler Power Level
        self.writeBoolean(False)

        self.writeString(self.player.bot4_n) # Bot 4 Name
        self.writeVint(2) # Enemy Star Player Type
        self.writeScId(16, self.player.bot4) # Bot 4 Brawler
        self.writeVint(0) # Bot 4 Skin
        self.writeVint(0) # Brawler Trophies
        self.writeVint(1) # Brawler Power Level
        self.writeBoolean(False)

        self.writeString(self.player.bot5_n) # Bot 5 Name
        self.writeVint(2) # Enemy Star Player Type
        self.writeScId(16, self.player.bot5) # Bot 5 Brawler
        self.writeVint(0) # Bot 5 Skin
        self.writeVint(0) # Brawler Trophies
        self.writeVint(1) # Brawler Power Level
        self.writeBoolean(False)

        # Experience Array
        self.writeVint(2) # Count
        self.writeVint(0) # Normal Experience ID
        self.writeVint(experience) # Normal Experience Ammount
        self.writeVint(8) # Star Player Experience ID
        self.writeVint(mvpexperience) # Star Player Experience Ammount

        # Rank Up and Level Up Bonus Array
        self.writeVint(0) # Count

        # Trophies and Experience Bars Array
        self.writeVint(2) # Count
        self.writeVint(1) # Ranks Milestone ID
        self.writeVint(brawler_trophies) # Brawler Trophies Bar
        self.writeVint(brawler_trophies_for_rank) # Brawler Trophies for Rank
        self.writeVint(5) # Experience Milestone ID
        self.writeVint(self.player.player_experience -experience -mvpexperience) # Player Experience Bar
        self.writeVint(self.player.player_experience -experience -mvpexperience) # Player Experience Bar for Level
        
        self.writeScId(28, self.player.profile_icon)  # Player Profile Icon (Unused since 2017)
        self.writeBoolean(True)  # Play Again