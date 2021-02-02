from Database.DatabaseManager import DataBase
from Packets.Messages.Server.Gameroom.TeamGameroomDataMessage import TeamGameroomDataMessage

from Utils.Reader import BSMessageReader

class LogicSetPlayerStarpowerCommand(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.player.starpower = self.read_Vint()


    def process(self):
        DataBase.replaceValue(self, 'starpower', self.player.starpower)
        if self.player.room_id > 0:
            TeamGameroomDataMessage(self.client, self.player).send()
