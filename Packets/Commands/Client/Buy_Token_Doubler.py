from Database.DataBase import DataBase
from Packets.Messages.Server.Gameroom.Team_Gameroom_Data_Message import TeamGameroomDataMessage

from Utils.Reader import BSMessageReader

class BuyTokenDoubler(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        pass



    def process(self):
        newGems = self.player.gems - 50
        DataBase.replaceValue(self, 'gems', newGems)
