from Database.DatabaseManager import DataBase

from Packets.Messages.Server.Gameroom.TeamLeftMessage import TeamLeftMessage

from Utils.Reader import BSMessageReader


class TeamLeaveMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        pass

    def process(self):
        TeamLeftMessage(self.client, self.player).send()
        DataBase.replaceGameroomValue(self, str(self.player.room_id), self.player.low_id, "removePlayer")
        DataBase.replaceValue(self, 'roomID', self.player.room_id)
        self.player.room_id = 0