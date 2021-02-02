from Packets.Messages.Server.Leaderboard.TopGlobalPlayersDataMessage import GetLeaderboardGlobalOkMessage
from Packets.Messages.Server.Leaderboard.TopLocalPlayersDataMessage import GetLeaderboardLocalOkMessage
from Packets.Messages.Server.Leaderboard.TopGlobalClubsDataMessage import GetLeaderboardClubGlobalOkMessage
from Packets.Messages.Server.Leaderboard.TopLocalClubsDataMessage import GetLeaderboardClubLocalOkMessage
from Database.DataBase import DataBase

from Utils.Reader import BSMessageReader


class GetLeaderboardMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.is_local = self.read_Vint()
        self.type = self.read_Vint()


    def process(self):
        if self.type == 1:

            def by_trophy(plr):
                return plr['trophies']

            players = DataBase.getAllPlayers(self)
            players.sort(key = by_trophy, reverse=True)

            if self.is_local == 1 or self.type == 0:
                GetLeaderboardLocalOkMessage(self.client, self.player, players).send()
            else:
                GetLeaderboardGlobalOkMessage(self.client, self.player, players).send()


        elif self.type == 2:
            if self.is_local == 1:
                GetLeaderboardClubLocalOkMessage(self.client, self.player, self.type).send()
            else:
                GetLeaderboardClubGlobalOkMessage(self.client, self.player, self.type).send()





