from Utils.Writer import Writer
from Database.DataBase import DataBase


class  GetLeaderboardClubGlobalOkMessage(Writer):

    def __init__(self, client, player, type):
        super().__init__(client)
        self.id = 24403
        self.player = player
        self.type = type

    def encode(self):
        self.writeVint(2)
        self.writeVint(0)
        self.writeVint(0)
        self.writeString("")

        self.writeVint(1) # Clubs Count

        self.writeVint(0) # Club High ID
        self.writeVint(1) # Club Low ID

        self.writeVint(1)
        self.writeVint(99999) # Club Trophies
        self.writeVint(2)

        self.writeString("Classic Brawl") # Club Name
        self.writeVint(1) # Club Members Count

        self.writeVint(8) # Club Badge
        self.writeVint(5) # Club Name Color


        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeString("RO")
