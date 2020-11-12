from Database.DataBase import DataBase

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
        self.player.roomID = 0
        DataBase.replaceValue(self, 'roomID', self.player.roomID)
        TeamLeftMessage(self.client, self.player).send()