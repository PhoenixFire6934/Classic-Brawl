from ByteStream.Reader import Reader
from Protocol.Messages.Server.AllianceListMessage import AllianceListMessage

class SearchAlliancesMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.query = self.readString()

    def process(self, db):
        result = []
        clubs = db.load_all_clubs({})

        for club in clubs:
            if self.query.lower() in club['Name'].lower():
                result.append(club)

        AllianceListMessage(self.client, self.player, self.query, result).send()


