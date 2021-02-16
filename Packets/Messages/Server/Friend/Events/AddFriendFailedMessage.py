from Utils.Writer import Writer

class AddFriendFailedMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 20112
        self.player = player

    def encode(self):
        self.writeInt(3) # Add friend 