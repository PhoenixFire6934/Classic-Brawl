from Utils.Writer import Writer


class PlayerProfileMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24113
        self.player = player

    def encode(self):
        self.writeVint(0)  # High Id
        self.writeVint(1)  # Low Id

        self.writeBoolean(False)

        self.writeVint(len(self.player.brawlers_id))  # Unlocked Brawlers Array

        for brawler_id in self.player.brawlers_id:
            self.writeScId(16, brawler_id)
            self.writeVint(0)
            self.writeVint(99999) # Brawler Trophies
            self.writeVint(99999) # Brawler Highest Trophies
            self.writeVint(10)    # Power Level

        self.writeVint(15) # Count

        self.writeVint(1)
        self.writeVint(99999)  # 3v3 Victories

        self.writeVint(2)
        self.writeVint(1262469) # Experience

        self.writeVint(3)
        self.writeVint(self.player.trophies)  # Trophies

        self.writeVint(4)
        self.writeVint(self.player.trophies)  # Highest Trophies

        self.writeVint(5)
        self.writeVint(len(self.player.brawlers_id)) # Brawlers Count

        self.writeVint(6)
        self.writeVint(0)

        self.writeVint(7)
        self.writeVint(99999)

        self.writeVint(8)
        self.writeVint(99999)  # Solo Victories

        self.writeVint(9)
        self.writeVint(99999)  # Best Robo Rumble Time

        self.writeVint(10)
        self.writeVint(99999)  # Best Time as Big Brawler

        self.writeVint(11)
        self.writeVint(99999)  # Duo Victories

        self.writeVint(12)
        self.writeVint(10)     # Highest Boss Fight Lvl Passed

        self.writeVint(13)
        self.writeVint(99999)

        self.writeVint(14)
        self.writeVint(1)      # Highest Power Play Rank

        self.writeVint(15)
        self.writeVint(99999)  # Most Challenge Wins


        self.writeString(self.player.name) # Player Name

        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)

        in_club = True

        if in_club:

            self.writeBoolean(True) # Player in Club

            self.writeInt(0) # Club High Id
            self.writeInt(1) # Club Low Id

            self.writeString("Classic Brawl") # Club Name

            self.writeVint(8)
            self.writeVint(5) # Badge ID

            self.writeVint(3)  # Club Type
            self.writeVint(2)  # Club Members Count

            self.writeVint(99999) # Club total trophies
            self.writeVint(99999) # Club required trophies
            self.writeVint(0)

            self.writeVint(0)
            self.writeVint(0)

        else:
            self.writeVint(0)
            self.writeVint(0)


