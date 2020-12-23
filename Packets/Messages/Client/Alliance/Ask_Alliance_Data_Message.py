from Packets.Messages.Server.Alliance.AllianceStreamMessage import AllianceStreamMessage
from Packets.Messages.Server.Alliance.AllianceDataMessage import AllianceDataMessage
from Database.DataBase import DataBase

from Utils.Reader import BSMessageReader


class Ask_Alliance_Data_Message(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.clubHighID = self.read_int()
        self.clubLowID = self.read_int()

    def process(self):
        AllianceDataMessage(self.client, self.player, self.clubHighID, self.clubLowID).send()