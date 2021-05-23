from Packets.Messages.Server.Home.PlayerProfileMessage import PlayerProfileMessage
from Database.DatabaseManager import DataBase

from Utils.Reader import BSMessageReader


class AskProfileMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.high_id = self.read_int()
        self.low_id = self.read_int()


    def process(self):
        self.players = DataBase.getAllPlayers(self)
       # if self.high_id == 0:
        PlayerProfileMessage(self.client, self.player, self.high_id, self.low_id, self.players).send()
