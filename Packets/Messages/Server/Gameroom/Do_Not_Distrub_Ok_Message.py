from Utils.Writer import Writer


class DoNotDistrubOkMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24111
        self.player = player

    def encode(self):
        self.writeVint(213)
        self.writeVint(self.player.DoNotDistrubMessage)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
