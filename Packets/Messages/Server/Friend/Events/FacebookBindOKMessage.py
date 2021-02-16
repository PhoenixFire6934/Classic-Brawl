from Utils.Writer import Writer

class FacebookBindOKMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24201
        self.player = player

    def encode(self):
        self.writeInt(0)