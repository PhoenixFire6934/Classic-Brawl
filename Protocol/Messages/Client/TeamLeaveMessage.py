from ByteStream.Reader import Reader
from Protocol.Messages.Server.TeamLeftMessage import TeamLeftMessage

class TeamLeaveMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        pass

    def process(self, db):
        TeamLeftMessage(self.client, self.player).send()