from ByteStream.Reader import Reader
from Protocol.Messages.Server.TeamMessage import TeamMessage

class TeamSetLocationMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.readVInt()
        self.player.map_id = self.readVInt()

    def process(self, db):
        TeamMessage(self.client, self.player).send()