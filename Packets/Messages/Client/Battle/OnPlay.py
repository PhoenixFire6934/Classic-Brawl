from Packets.Messages.Server.OutOfSyncMessage import OutOfSyncMessage

from Utils.Reader import BSMessageReader


class OnPlay(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client


    def decode(self):
        self.read_Vint()
        self.CardID = self.read_Vint()

        self.read_Vint()
        self.MapIndex = self.read_Vint()

        print(self.CardID, self.MapIndex)

    def process(self):
        pass