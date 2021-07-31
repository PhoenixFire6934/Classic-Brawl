from ByteStream.Reader import Reader
from Logic.Home.LogicShopData import LogicShopData

class LogicPurchaseHeroLvlUpMaterialCommand(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.readVInt()
        self.readVInt()
        self.readLogicLong()
        self.gold_value = self.readVInt()


    def process(self, db):

        self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + LogicShopData.gold_packs[self.gold_value]['Amount']
        db.update_player_account(self.player.token, 'Resources', self.player.resources)

        self.player.gems = self.player.gems - LogicShopData.gold_packs[self.gold_value]['Cost']
        db.update_player_account(self.player.token, 'Gems', self.player.gems)
