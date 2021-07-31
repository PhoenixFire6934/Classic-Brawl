from ByteStream.Reader import Reader
from Utils.Helpers import Helpers
from Logic.Home.LogicShopData import LogicShopData
from Protocol.Messages.Server.AvailableServerCommandMessage import AvailableServerCommandMessage

class LogicGatchaCommand(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.readVInt()
        self.readVInt()
        self.readLogicLong()
        self.box_id = self.readVInt()


    def process(self, db):
        self.player.delivery_items = {'Count': 1, 'Type': Helpers.get_box_type(self, self.box_id)}

        if self.box_id == 1:
            self.player.gems = self.player.gems - LogicShopData.boxes[0]['Cost']
            db.update_player_account(self.player.token, 'Gems', self.player.gems)
        elif self.box_id == 3:
            self.player.gems = self.player.gems - LogicShopData.boxes[1]['Cost']
            db.update_player_account(self.player.token, 'Gems', self.player.gems)

        self.player.db = db
        AvailableServerCommandMessage(self.client, self.player, 203).send()



