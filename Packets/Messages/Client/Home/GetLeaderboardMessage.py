from Packets.Messages.Server.Home.PlayerProfileMessage import PlayerProfileMessage
from Packets.Messages.Server.Home.GetLeaderboardOkMessage import GetLeaderboardOkMessage

from Utils.Reader import BSMessageReader


class GetLeaderboardMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        pass


    def process(self):
        GetLeaderboardOkMessage(self.client, self.player).send()

