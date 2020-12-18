from Utils.Writer import Writer


class AllianceDataMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24301
        self.player = player

    def encode(self):
        self.writeVint(1)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeInt(1)
        self.writeString("Classic Brawl") # club name
        self.writeVint(8)
        self.writeVint(5) # badge ID
        self.writeVint(3) # club type [1 = open, 2 = invite only, 3 = closed]
        self.writeVint(1) # members count
        self.writeVint(self.player.trophies) # required trophies
        self.writeVint(0)
        self.writeVint(0)
        self.writeString("RO") # region
        self.writeVint(0)
        self.writeVint(0)
        self.writeString("The best Brawl Stars server emulator!") # desc
        self.writeVint(1)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0) # High Id
        self.writeInt(1)  # Low Id
        self.writeVint(2)
        self.writeVint(self.player.trophies)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeString(self.player.name)
        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)

        self.writeVint(-1)
        self.writeVint(-1040385)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
