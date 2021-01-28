from Database.DataBase import DataBase
from Packets.Commands.Server.LogicBoxDataCommand import LogicBoxDataCommand

from Utils.Reader import BSMessageReader

class LogicPurchaseBoxCommand(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.player.box_id = self.read_Vint()


    def process(self):
        LogicBoxDataCommand(self.client, self.player).send()
