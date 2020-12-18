from Utils.Writer import Writer


class BotProfileMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24113
        self.player = player

    def encode(self):
        self.writeVint(1)  # High Id
        self.writeVint(1)  # Low Id
        self.writeVint(0)

        self.writeVint(len(self.player.brawlers_id))  # brawlers array

        for brawler_id in self.player.brawlers_id:
            self.writeScId(16, brawler_id)
            self.writeVint(0)
            self.writeVint(99999)
            self.writeVint(99999)
            self.writeVint(10) # power lvl


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

        self.writeVint(len(self.player.brawlers_id) - 1)
        self.writeVint(len(self.player.brawlers_id) - 1)

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
        self.writeString("Bot")
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
