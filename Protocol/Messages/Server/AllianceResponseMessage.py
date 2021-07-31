from ByteStream.Writer import Writer

class AllianceResponseMessage(Writer):

    def __init__(self, client, player, action):
        super().__init__(client)
        self.id = 24333
        self.player = player
        self.action = action

    def encode(self):
        self.writeVInt(self.action)