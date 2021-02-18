from Utils.Writer import Writer

class FriendListUpdateMessage(Writer):

    def __init__(self, client, player, friendLowID):
        super().__init__(client)
        self.id = 20106
        self.player = player
        self.friendID = friendLowID

    def encode(self):
        self.writeVint(2)

        self.writeInt(0)  # HighID
        self.writeInt(1)  # LowID


        if False:
            #self.writeInt(25)
            self.writeVint(9339)
            self.writeString("192.168.1.98")

            self.writeInt(10)

            self.writeInt(0)
            self.writeInt(1)

            self.writeInt(0)
            self.writeInt(self.player.low_id)

            self.writeString("hi-kfP1ub1HxoZFsLLVNmxD0zYxWWMmtpZY_EwE88uw")
            #self.writeInt(0) # HighID
            #self.writeInt(323426908) # LowID