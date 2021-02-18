from Utils.Writer import Writer

class AddableFriendsMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 20199
        self.player = player

    def encode(self):
        self.writeInt(1)
        self.writeInt(1)

        self.writeInt(0)  # HighID
        self.writeInt(1)  # LowID

        self.writeString("romashka") # Player name

        self.writeString() # FacebookID
        self.writeString()
        self.writeString()
        # Friend state 0 = friend, 1 = not friend, 2 = request sent, 3 = you have an invite from him??, 4 = friend list
        self.writeInt(3)
        self.writeInt(1000) # Trophies
        self.writeInt(3)
        self.writeInt(3)
        self.writeInt(3)
        self.writeInt(3)

        self.writeBoolean(False) # Club

        self.writeString()
        self.writeInt(0)
        self.writeInt(0)