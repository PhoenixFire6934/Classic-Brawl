from ByteStream.Reader import Reader
from Protocol.Messages.Server.PlayerProfileMessage import PlayerProfileMessage


class GetPlayerProfileMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.account_id = self.readLong()

    def process(self, db):
        account_data = db.load_player_account_by_id(self.account_id)

        PlayerProfileMessage(self.client, self.player, account_data, db).send()