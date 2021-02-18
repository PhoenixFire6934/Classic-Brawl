from Utils.Writer import Writer


class UnknownServerPackets(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24261
        self.player = player

    def encode(self):
        self.writeString("HEl")
