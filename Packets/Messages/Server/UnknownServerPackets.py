from Utils.Writer import Writer


class UnknownServerPackets(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24131
        self.player = player

    def encode(self):
        self.writeVint(2)
        self.writeVint(0)
        self.writeVint(1)
        self.writeVint(1)
        self.writeVint(1)
        self.writeString("Gaby")
        self.writeVint(1)
        self.writeVint(0)
        self.writeString("Hey")

