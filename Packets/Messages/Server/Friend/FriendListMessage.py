from Utils.Writer import Writer

class FriendListMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 20105
        self.player = player

    def encode(self):
        self.writeInt(1)
        self.writeVint(0)
        self.writeInt(1)

        self.writeInt(0)  # HighID
        self.writeInt(1)  # LowID

        self.writeString("Player") # Player name

        self.writeString() # FacebookID
        self.writeString()
        self.writeString()

        self.writeInt(4)
        self.writeInt(1000) # Trophies
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)

        self.writeBoolean(False) # Club

        self.writeString()
        self.writeInt(28)
        self.writeInt(0)