from Utils.Writer import Writer
from Database.DatabaseManager import DataBase


class GetLeaderboardGlobalOkMessage(Writer):

    def __init__(self, client, player, players, LocalIndex):
        super().__init__(client)
        self.id = 24403
        self.player = player
        self.players = players
        self.LocalIndex = LocalIndex

    def encode(self):
        self.writeVint(1)
        self.writeVint(0) # SCID
        self.writeString()

        self.writeVint(len(self.players)) # Players Count

        for player in self.players:

            self.writeVint(0) # High ID
            self.writeVint(player['lowID']) # Low ID

            self.writeVint(1)
            self.writeVint(player['trophies']) # Player Trophies

            self.writeBoolean(True) # Player data boolean
            self.writeString(player['name'])  # Player Name

            if player['clubID'] > 0:
                DataBase.loadClub(self, player['clubID'])
                self.writeString(self.clubName)  # Club Name
            else:
                self.writeString()  # Club Name

            self.writeVint(1) # Player Level
            self.writeScId(28, player['profileIcon'])

            self.writeBoolean(False)

        self.writeVint(0)
        self.writeVint(self.LocalIndex)
        self.writeVint(0)
        self.writeVint(0)
        self.writeString("RO")