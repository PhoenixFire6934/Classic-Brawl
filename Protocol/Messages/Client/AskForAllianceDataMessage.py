from ByteStream.Reader import Reader
from Protocol.Messages.Server.AllianceDataMessage import AllianceDataMessage

class AskForAllianceDataMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.club_id = self.readLong()

    def process(self, db):
        club_data = db.load_club(self.club_id)

        AllianceDataMessage(self.client, self.player, club_data).send()