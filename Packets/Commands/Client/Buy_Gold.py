from Database.DataBase import DataBase
from Packets.Messages.Server.Gameroom.Team_Gameroom_Data_Message import TeamGameroomDataMessage

from Utils.Reader import BSMessageReader

class BuyGold(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.gold = self.read_Vint()


    def process(self):
        if self.gold == 0:
            newGold = self.player.gold + 150
            newGems = self.player.gems - 20
            DataBase.replaceValue(self, 'gold', newGold)
            DataBase.replaceValue(self, 'gems', newGems)
        elif self.gold == 1:
            newGold = self.player.gold + 400
            newGems = self.player.gems - 50
            DataBase.replaceValue(self, 'gold', newGold)
            DataBase.replaceValue(self, 'gems', newGems)
        elif self.gold == 2:
            newGold = self.player.gold + 1200
            newGems = self.player.gems - 140
            DataBase.replaceValue(self, 'gold', newGold)
            DataBase.replaceValue(self, 'gems', newGems)
