from Packets.Messages.Server.Battle.MatchMakingCancelledMessage import MatchMakingCancelledMessage


from Utils.Reader import BSMessageReader


class PlayerStatusMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client


    def decode(self):
        self.status = self.read_Vint()

    def process(self):
        if self.status == 4 or self.status == 12:
            MatchMakingCancelledMessage(self.client, self.player).send()

