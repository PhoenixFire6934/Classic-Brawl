from Utils.Writer import Writer

class FriendListMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 20105
        self.player = player

    def encode(self):
        self.writeVint(1)
        self.writeVint(1)

        self.writeInt(0)  # HighID
        self.writeInt(1)  # LowID

        self.writeString()
        self.writeString()
        self.writeString()
        self.writeString()
        self.writeString()
        self.writeString()

        self.writeInt(1000)  # Trophies
        self.writeInt(4)  # Friend state 0 = friend, 1 = not friend, 2 = request sent, 3 = you have an invite from him??, 4 = friend list
        self.writeInt(1)
        self.writeInt(1)
        self.writeInt(1)

        self.writeBoolean(False)

        self.writeString()
        self.writeInt(0)

        self.writeBoolean(True)  # ?? is a player?

        self.writeString("Friendly bot")
        self.writeVint(100)
        self.writeVint(28000005)
        self.writeVint(43000002)
        self.writeVint(0)
