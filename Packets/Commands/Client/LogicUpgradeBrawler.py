from Database.DatabaseManager import DataBase

from Utils.Reader import BSMessageReader

class Upgrade_Brawler(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()                  # csvID
        self.BrawlerID = self.read_Vint() # BrawlerID


    def process(self):
        self.player.Brawler_level[str(self.BrawlerID)] += 1
        DataBase.replaceValue(self, 'brawlerPowerLevel', self.player.Brawler_level)
        
        #if self.player.Brawler_level[str(self.BrawlerID)] == 1:
         #   DataBase.replaceValue(self, 'gold', self.player.gold -20)
        #elif self.player.Brawler_level[str(self.BrawlerID)] == 2:
         #   DataBase.replaceValue(self, 'gold', self.player.gold -35)
       # elif self.player.Brawler_level[str(self.BrawlerID)] == 3:
        #    DataBase.replaceValue(self, 'gold', self.player.gold -75)
        #elif self.player.Brawler_level[str(self.BrawlerID)] == 4:
         #   DataBase.replaceValue(self, 'gold', self.player.gold -140)
        #elif self.player.Brawler_level[str(self.BrawlerID)] == 5:
         #   DataBase.replaceValue(self, 'gold', self.player.gold -290)
        #elif self.player.Brawler_level[str(self.BrawlerID)] == 6:
         #   DataBase.replaceValue(self, 'gold', self.player.gold -480)
        #elif self.player.Brawler_level[str(self.BrawlerID)] == 7:
         #   DataBase.replaceValue(self, 'gold', self.player.gold -800)
        #elif self.player.Brawler_level[str(self.BrawlerID)] == 8:
         #   DataBase.replaceValue(self, 'gold', self.player.gold -1250)