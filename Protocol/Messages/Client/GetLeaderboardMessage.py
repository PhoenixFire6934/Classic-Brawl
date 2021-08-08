from ByteStream.Reader import Reader
from Protocol.Messages.Server.LeaderboardMessage import LeaderboardMessage


class GetLeaderboardMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.readBool()
        self.readVInt()
        self.type = self.readVInt()


    def process(self, db):
        if  self.type == 1:
            self.player.leaderboard_type = 1
            players = db.load_all_players_sorted({}, 'Trophies')
            players.reverse()

            LeaderboardMessage(self.client, self.player, players).send()

        elif self.type == 2:
            self.player.leaderboard_type = 2
            clubs = db.load_all_clubs_sorted({}, 'Trophies')
            clubs.reverse()

            LeaderboardMessage(self.client, self.player, clubs).send()
