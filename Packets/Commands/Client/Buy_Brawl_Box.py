from Database.DataBase import DataBase
from Packets.Commands.Server.Buy_Brawl_Box_Callback import BuyBrawlBoxCallback

from Utils.Reader import BSMessageReader

class BuyBrawlBox(BSMessageReader):
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
        BuyBrawlBoxCallback(self.client, self.player).send()
