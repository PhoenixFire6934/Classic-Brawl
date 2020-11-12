from Utils.Writer import Writer


class PlayerProfileMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24113
        self.player = player

    def encode(self):
        self.writeVint(0)  # High Id
        self.writeVint(1)  # Low Id
        self.writeVint(0)

        self.writeVint(35)  # brawlers array

        for i in range(0, 33):
            self.writeVint(16)
            self.writeVint(i)
            self.writeVint(0)
            self.writeVint(99999)
            self.writeVint(99999)
            self.writeVint(2)

        # exceptions
        self.writeVint(16)
        self.writeVint(34)
        self.writeVint(0)
        self.writeVint(99999)
        self.writeVint(99999)
        self.writeVint(2)

        self.writeVint(16)
        self.writeVint(37)
        self.writeVint(0)
        self.writeVint(99999)
        self.writeVint(99999)
        self.writeVint(2)

        self.writeVint(14)
        self.writeVint(1)
        self.writeVint(99999)  # 3v3 victories
        self.writeVint(2)
        self.writeVint(1262469)
        self.writeVint(3)
        self.writeVint(99999)
        self.writeVint(4)
        self.writeVint(self.player.trophies)  # highest trophies
        self.writeVint(5)

        self.writeVint(34)
        self.writeVint(34)

        self.writeVint(28000000)
        self.writeVint(8)
        self.writeVint(99999)  # solo victories
        self.writeVint(9)
        self.writeVint(21)
        self.writeVint(10)
        self.writeVint(99999)
        self.writeVint(11)
        self.writeVint(99999)  # duo victories
        self.writeVint(12)
        self.writeVint(21)
        self.writeVint(13)
        self.writeVint(99999)
        self.writeVint(14)
        self.writeVint(1)
        self.writeVint(15)
        self.writeVint(99999)  # most challenge wins
        self.writeString(self.player.name)
        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(-1040385)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
