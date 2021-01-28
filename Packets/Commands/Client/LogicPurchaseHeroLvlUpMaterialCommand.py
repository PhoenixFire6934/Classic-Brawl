from Database.DataBase import DataBase
from Logic.Shop import Shop

from Utils.Reader import BSMessageReader

class LogicPurchaseHeroLvlUpMaterialCommand(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.gold = self.read_Vint()


    def process(self):
        cost = Shop.gold[self.gold]['Cost']
        value = Shop.gold[self.gold]['Amount']

        newGold = self.player.gold + value
        self.player.gold = newGold
        newGems = self.player.gems - cost
        self.player.gems = newGems

        DataBase.replaceValue(self, 'gold', newGold)
        DataBase.replaceValue(self, 'gems', newGems)

