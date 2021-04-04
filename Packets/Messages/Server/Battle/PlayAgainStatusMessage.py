from Utils.Writer import Writer


class PlayAgainStatusMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24777
        self.player = player

    def encode(self):
        self.writeInt(3) # 0 = Waiting, 1 = crash ?, 2 = Matchmaking 
        self.writeVint(2) # ??