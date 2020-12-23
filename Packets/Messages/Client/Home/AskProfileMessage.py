from Packets.Messages.Server.Home.PlayerProfileMessage import PlayerProfileMessage
from Packets.Messages.Server.AllianceBot.AllianceBotProfileMessage import BotProfileMessage

from Utils.Reader import BSMessageReader


class AskProfileMessage(BSMessageReader):
    def __init__(self, client, player, initial_byte):
        super().__init__(initial_byte)
        self.player = player
        self.client = client

    def decode(self):
        self.high_id = self.read_int() 
        self.low_id = self.read_int()


    def process(self):
        print("Printed by AskProfileMessage", "High id:", self.high_id, "Low id:", self.low_id)
        
        PlayerProfileMessage(self.client, self.player, self.high_id, self.low_id).send()