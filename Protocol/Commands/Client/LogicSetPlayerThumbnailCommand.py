from ByteStream.Reader import Reader

class LogicSetPlayerThumbnailCommand(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.readVInt()
        self.readVInt()
        self.readLogicLong()
        self.player.profile_icon = self.readDataReference()[1]

    def process(self, db):
        db.update_player_account(self.player.token, 'ProfileIcon', self.player.profile_icon)