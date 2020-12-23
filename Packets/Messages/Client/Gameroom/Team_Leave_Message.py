from Database.DataBase import DataBase

from Packets.Messages.Server.Gameroom.Team_Left_Message import TeamLeftMessage

from Utils.Reader import BSMessageReader


class TeamLeaveMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        pass

    def process(self):
        self.player.room_id = 0
        DataBase.replaceValue(self, 'roomID', self.player.room_id)
        TeamLeftMessage(self.client, self.player).send()