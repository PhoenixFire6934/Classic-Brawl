from Utils.Writer import Writer
from Database.DataBase import DataBase

class MatchMakingCancelledMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 20406
        self.player = player


    def encode(self):
        pass



