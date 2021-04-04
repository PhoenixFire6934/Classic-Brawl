from Utils.Writer import Writer
from Database.DatabaseManager import DataBase


class BattleResultTutorialMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 23456
        self.player = player

    def encode(self):
        brawler_trophies = self.player.brawlers_trophies[str(self.player.brawler_id)]
        brawler_trophies_for_rank = self.player.brawlers_trophies_in_rank[str(self.player.brawler_id)]
        if self.player.Brawler_starPower[str(self.player.brawler_id)] >= 1:
            brawler_level = self.player.Brawler_level[str(self.player.brawler_id)] + 2
        else:
            brawler_level = self.player.Brawler_level[str(self.player.brawler_id)] + 1

        self.writeVint(0)
        self.writeVint(self.player.battle_result)

        if self.player.battle_result == 0:
            self.player.tutorial += 1
            DataBase.replaceValue(self, 'tutorial', self.player.tutorial)
        else: 
            self.player.tutorial = 0

        self.writeVint(0) # Tokens Gained
        self.writeVint(0) # Trophies Result 
        self.writeVint(0) # Doubled Tokens
        self.writeVint(0) # Token Doubler Remaining
        self.writeVint(0) # Big Game/Robo Rumble Time
        self.writeVint(32) # Battle Result Info and Stuff
        self.writeVint(self.player.players) #Battle End Screen Players

        self.writeString(self.player.name) # Player Name
        self.writeVint(1) # Self Star Player Type
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
