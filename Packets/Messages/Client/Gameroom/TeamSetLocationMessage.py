from Packets.Messages.Server.Gameroom.TeamGameroomDataMessage import TeamGameroomDataMessage
from Database.DatabaseManager import DataBase

from Utils.Reader import BSMessageReader

class TeamSetLocationMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.read_Vint()
        self.player.map_id = self.read_Vint()
        self.roomType = 1

    def process(self):
        DataBase.replaceGameroomValue(self, 'mapID', self.player.map_id, "room")
        DataBase.replaceGameroomValue(self, 'roomType', self.roomType, "room")
        TeamGameroomDataMessage(self.client, self.player).send()