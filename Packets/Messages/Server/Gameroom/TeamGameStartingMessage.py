from Utils.Writer import Writer


class TeamGameStartingMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24130
        self.player = player

    def encode(self):
        self.writeVint(0)
        self.writeVint(0)
    
        self.writeVint(23)
        self.writeVint(0)