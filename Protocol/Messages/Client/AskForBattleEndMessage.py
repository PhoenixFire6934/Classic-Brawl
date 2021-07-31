from ByteStream.Reader import Reader
from Protocol.Messages.Server.BattleEndMessage import BattleEndMessage

class AskForBattleEndMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client
        self.players = {}

    def decode(self):
        self.result   = self.readVInt()
        self.unk      = self.readVInt()
        self.rank     = self.readVInt()
        self.mapID    = self.readDataReference()

        self.count    = self.readVInt()

        for player in range(self.count):
            self.brawler     = self.readDataReference()
            self.skin        = self.readDataReference()
            self.team        = self.readVInt()
            self.unk         = self.readVInt()
            self.username    = self.readString()

            self.players[player] = {f'Name': self.username, 'Team': self.team, 'Brawler': self.brawler[1], 'Skin': self.skin[1]}


    def process(self, db):
        if self.rank != 0:
            if self.players[0]['Team'] == self.players[1]['Team']:
                self.type = 5
            else:
                self.type = 2
        else:
            self.type = 0

        BattleEndMessage(self.client, self.player, self.type, self.result, self.players).send()




