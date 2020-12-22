from Utils.Writer import Writer


class MyAllianceMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24399
        self.player = player

    def encode(self):
        self.writeVint(2) # Members Count
        self.writeVint(1)
        self.writeVint(25)

        self.writeVint(2)

        self.writeInt(0) # Club High Id
        self.writeInt(1) # Club Low Id

        self.writeString("Classic Brawl") # Club Name

        self.writeVint(8)
        self.writeVint(5) # Badge ID

        self.writeVint(3)  # Club Type
        self.writeVint(2)  # Club Members Count

        self.writeVint(self.player.trophies)
        self.writeVint(self.player.trophies)

        self.writeVint(0)
        self.writeString("RO")  # Region

        self.writeVint(0)
        self.writeVint(0)
