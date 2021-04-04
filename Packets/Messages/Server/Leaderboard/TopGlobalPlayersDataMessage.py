from Utils.Writer import Writer
from Database.DatabaseManager import DataBase


class GetLeaderboardGlobalOkMessage(Writer):

    def __init__(self, client, player, players):
        super().__init__(client)
        self.id = 24403
        self.player = player
        self.players = players

    def encode(self):
        self.indexOfPlayer = 1
        self.writeVint(1)
        self.writeVint(0) # SCID
        self.writeString()

        self.writeVint(len(self.players)) # Players Count

        for player in self.players:
            if player["lowID"] == self.player.low_id:
                self.indexOfPlayer = self.players.index(player) + 1
            self.writeVint(0) # High ID
            self.writeVint(player["lowID"]) # Low ID

            self.writeVint(1)
            self.writeVint(player['trophies']) # Player Trophies

            self.writeVint(1)

            self.writeString(player['name']) 
            if player["clubID"] != 0:
                DataBase.loadClub(self, player["clubID"])
                self.writeString(self.clubName)
            else:
                self.writeString()

            self.writeVint(player['playerExp']) # Player Experience Level
            self.writeScId(28, player['profileIcon'])  # Player Profile Icon
            self.writeVint(0)


        self.writeVint(0)
        self.writeVint(self.indexOfPlayer)
        self.writeVint(0)
        self.writeVint(0) # Leaderboard Region
        self.writeString(self.player.region)
        print("[INFO] Message LeaderboardMessage has been sent.")
