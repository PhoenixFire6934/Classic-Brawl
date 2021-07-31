from ByteStream.Reader import Reader
from Protocol.Messages.Server.AvatarNameCheckResponseMessage import AvatarNameCheckResponseMessage

class AvatarNameCheckRequestMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.username = self.readString()

    def process(self, db):
        AvatarNameCheckResponseMessage(self.client, self.player, self.username).send()