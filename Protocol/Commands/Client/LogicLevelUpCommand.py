from ByteStream.Reader import Reader

class LogicLevelUpCommand(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.readVInt()
        self.readVInt()
        self.readLogicLong()
        self.brawler = self.readDataReference()[1]

    def process(self, db):
        self.player.brawlers_level[str(self.brawler)] = self.player.brawlers_level[str(self.brawler)] + 1
        db.update_player_account(self.player.token, 'BrawlersLevel', self.player.brawlers_level)
