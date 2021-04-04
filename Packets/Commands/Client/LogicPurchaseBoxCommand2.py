from Database.DatabaseManager import DataBase
from Packets.Commands.Server.LogicBoxDataCommand import LogicBoxDataCommand

from Utils.Reader import BSMessageReader

class LogicPurchaseBoxCommand2(BSMessageReader):
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
        if self.player.box_id == 5:
            DataBase.replaceValue(self, 'brawlBoxes', self.player.brawl_boxes - 100)
            LogicBoxDataCommand(self.client, self.player).send()
        elif self.player.box_id == 4:
            DataBase.replaceValue(self, 'bigBoxes', self.player.big_boxes - 10)
            LogicBoxDataCommand(self.client, self.player).send()
        elif self.player.box_id == 3:
            DataBase.replaceValue(self, 'gems', self.player.gems - 80)
            LogicBoxDataCommand(self.client, self.player).send()
        elif self.player.box_id == 2:
            DataBase.replaceValue(self, 'gems', self.player.gems - 30)
            LogicBoxDataCommand(self.client, self.player).send()
