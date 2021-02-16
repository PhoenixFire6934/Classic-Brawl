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