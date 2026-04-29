from ByteStream.Reader import Reader
from Utils.Helpers import Helpers
from Logic.Home.LogicShopData import LogicShopData
from Protocol.Messages.Server.AvailableServerCommandMessage import AvailableServerCommandMessage
from Protocol.Commands.Server.LogicGiveDeliveryItemsCommand import LogicGiveDeliveryItemsCommand

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
        print(f"[DEBUG] Box ID from client: {self.box_id}")
        box_type = Helpers.get_box_type(self.box_id)
        print(f"[DEBUG] Box type: {box_type}")
    
        self.player.delivery_items = {'Count': 1, 'DeliveryTypes': [box_type]}

        if self.box_id == 1:  # Shop Big Box (gems)
            self.player.gems -= LogicShopData.boxes[0]['Cost']
            db.update_player_account(self.player.token, 'Gems', self.player.gems)
        elif self.box_id == 3:  # Shop Mega Box (gems)
            self.player.gems -= LogicShopData.boxes[1]['Cost']
            db.update_player_account(self.player.token, 'Gems', self.player.gems)
        elif self.box_id == 5:  # Brawl Box (tokens)
            # We write off 100 tokens (BrawlBoxTokens)
            self.player.resources[0]['Amount'] -= 100
            db.update_player_account(self.player.token, 'Resources', self.player.resources)
        elif self.box_id == 4:  # Big Box (за токены)
            # We write off 10 tokens (BigBoxTokens)
            self.player.resources[2]['Amount'] -= 10  # ID 9 = BigBoxTokens
            db.update_player_account(self.player.token, 'Resources', self.player.resources)

        self.player.db = db
        AvailableServerCommandMessage(self.client, self.player, LogicGiveDeliveryItemsCommand).send()