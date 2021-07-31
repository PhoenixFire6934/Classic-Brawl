from ByteStream.Reader import Reader
from Protocol.Messages.Server.JoinableAllianceListMessage import JoinableAllianceListMessage

class AskForJoinableAlliancesListMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        pass

    def process(self, db):
        clubs = db.load_all_clubs_sorted({}, 'Trophies')

        JoinableAllianceListMessage(self.client, self.player, clubs).send()