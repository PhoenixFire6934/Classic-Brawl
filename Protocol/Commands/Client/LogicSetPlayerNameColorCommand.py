from ByteStream.Reader import Reader

class LogicSetPlayerNameColorCommand(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.readVInt()
        self.readVInt()
        self.readLogicLong()
        self.player.name_color = self.readDataReference()[1]

    def process(self, db):
        db.update_player_account(self.player.token, 'NameColor', self.player.name_color)