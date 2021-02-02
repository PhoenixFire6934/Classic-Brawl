from Database.DatabaseManager import DataBase
from Logic.Shop import Shop
from Packets.Messages.Server.Gameroom.TeamGameroomDataMessage import TeamGameroomDataMessage

from Utils.Reader import BSMessageReader

class LogicPurchaseDoubleCoinsCommand(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        pass


    def process(self):
        cost = Shop.token_doubler['Cost']
        value = Shop.token_doubler['Amount']

        newGems = self.player.gems - cost
        self.player.gems = newGems
        DataBase.replaceValue(self, 'gems', newGems)

        newTokens = self.player.tokens + value
        self.player.tokens = newTokens
        DataBase.replaceValue(self, 'tokens', newTokens)

