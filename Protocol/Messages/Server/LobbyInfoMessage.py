from ByteStream.Writer import Writer

class LobbyInfoMessage(Writer):

    def __init__(self, client, player, count):
        super().__init__(client)
        self.id = 23457
        self.player = player
        self.count = count

    def encode(self):
        self.writeVInt(self.count)
        self.writeString("Classic Brawl v2.0")

        self.writeVInt(0) # array
        for x in range(0):
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
