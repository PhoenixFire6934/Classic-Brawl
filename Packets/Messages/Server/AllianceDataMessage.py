from Utils.Writer import Writer


class ClubProfileMessage(Writer):

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
        self.writeString("Classic Brawl")
        self.writeVint(8)
        self.writeVint(5)
        self.writeVint(3)
        self.writeVint(1)
        self.writeVint(self.player.trophies)
        self.writeVint(0)
        self.writeVint(0)
        self.writeString("RO")
        self.writeVint(0)
        self.writeVint(0)
        self.writeString("The best Brawl Stars server emulator!")
        self.writeVint(1)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)  # High Id
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
        print("[INFO] Message ClubProfileMessage has been sent.")