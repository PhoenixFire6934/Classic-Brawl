from Utils.Writer import Writer


class AllianceDataMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24301
        self.player = player

    def encode(self):
        self.writeVint(1)

        self.writeInt(0) # Club High Id
        self.writeInt(1) # Club Low Id

        self.writeString("Classic Brawl") # Club Name

        self.writeVint(8)
        self.writeVint(5) # Badge ID

        self.writeVint(3) # Club Type [1 = open, 2 = invite only, 3 = closed]

        self.writeVint(2) # Members Count

        self.writeVint(self.player.trophies) # Required Trophies
        self.writeVint(0)
        self.writeVint(0)
        self.writeString("RO") # Region
        self.writeVint(0)
        self.writeVint(0)
        self.writeString("The best Brawl Stars server emulator!") # desc

        self.writeVint(2) # Members List Count

        self.writeInt(0)  # Player High Id
        self.writeInt(1)  # Player Low Id
        self.writeVint(2)
        self.writeVint(self.player.trophies)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeString(self.player.name)
        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)

        self.writeInt(1)  # Bot High Id
        self.writeInt(1)  # Bot Low Id
        self.writeVint(2)
        self.writeVint(99999)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeString("Club Bot")
        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)


