from ByteStream.Writer import Writer

class AvatarNameChangeFailedMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 20205
        self.player = player

    def encode(self):
        self.writeVInt(0)