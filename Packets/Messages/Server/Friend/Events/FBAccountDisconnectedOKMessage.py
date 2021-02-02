from Utils.Writer import Writer

class FBAccountDisconnectedOKMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24214
        self.player = player

    def encode(self):
        pass