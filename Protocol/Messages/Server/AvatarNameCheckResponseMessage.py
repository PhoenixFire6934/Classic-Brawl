from ByteStream.Writer import Writer

class AvatarNameCheckResponseMessage(Writer):

    def __init__(self, client, player, username):
        super().__init__(client)
        self.id = 20300
        self.player = player
        self.username = username

    def encode(self):
        self.writeUInt8(0)
        self.writeInt(0)
        self.writeString(self.username)