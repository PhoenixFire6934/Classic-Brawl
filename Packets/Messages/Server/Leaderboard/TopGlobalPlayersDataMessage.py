from Utils.Writer import Writer
from Database.DatabaseManager import DataBase


class GetLeaderboardGlobalOkMessage(Writer):

    def __init__(self, client, player, players):
        super().__init__(client)
        self.id = 24403
        self.player = player
        self.players = players

    def encode(self):
        self.writeBoolean(True)
        self.writeVint(0)
        self.writeVint(0)
        self.writeString()


        self.writeVint(len(self.players)) # Players Count

        for player in self.players:

            self.writeVint(0) # High ID
            self.writeVint(1) # Low ID

            self.writeVint(1)
            self.writeVint(player['trophies']) # Player Trophies

            self.writeVint(1)

            self.writeString() # Club Name
            self.writeString(player['name']) # Player Name

            self.writeVint(1) # Player Level
            self.writeVint(28000000 + player['profileIcon'])
            self.writeVint(43000000 + player['namecolor'])
            self.writeVint(0)


        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeString("RO")
