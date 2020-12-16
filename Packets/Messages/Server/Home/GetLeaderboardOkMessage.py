from Utils.Writer import Writer
from Database.DataBase import DataBase


class GetLeaderboardOkMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24403
        self.player = player

    def encode(self):
        self.writeVint(1)
        self.writeVint(0)
        self.writeVint(0)

        self.writeString()

        players = DataBase.getAllPlayers(self)

        self.writeVint(len(players)) # players count

        for player in players:

            self.writeVint(0) # high ID
            self.writeVint(1) # low ID

            self.writeVint(1)

            self.writeVint(player['trophies']) # trophies

            self.writeVint(1)

            self.writeString()

            self.writeString(player['name'])

            self.writeVint(1)
            self.writeVint(28000000 + player['profileIcon'])
            self.writeVint(43000000 + player['namecolor'])
            self.writeVint(0)


        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeString("RO")