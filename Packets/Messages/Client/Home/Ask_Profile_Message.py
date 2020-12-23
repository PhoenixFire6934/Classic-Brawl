from Packets.Messages.Server.Home.Player_Profile_Message import PlayerProfileMessage
from Packets.Messages.Server.AllianceBot.Alliance_Bot_Profile_Message import BotProfileMessage

from Utils.Reader import BSMessageReader


class AskProfileMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.high_id = self.read_Vint()


    def process(self):
        if self.high_id == 0:
            PlayerProfileMessage(self.client, self.player).send()
        else:
            BotProfileMessage(self.client, self.player).send()
