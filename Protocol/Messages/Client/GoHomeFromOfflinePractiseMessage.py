from ByteStream.Reader import Reader
from Protocol.Messages.Server.OwnHomeDataMessage import OwnHomeDataMessage

class GoHomeFromOfflinePractiseMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        pass

    def process(self, db):
        OwnHomeDataMessage(self.client, self.player).send()