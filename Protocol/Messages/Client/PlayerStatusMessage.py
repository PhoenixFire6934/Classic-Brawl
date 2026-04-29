from ByteStream.Reader import Reader

class PlayerStatusMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client
        self.status: int = 0

    def decode(self):
        self.status = self.readVInt()

    def process(self, db):
        if self.status == self.player.status: 
            return
        
        if self.status == 4294967295: 
            self.status = 8
        
        self.player.status = self.status