from Utils.Writer import Writer
from Database.DatabaseManager import DataBase

class ChangeNameCallback(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24111
        self.player = player

    def encode(self):
        self.writeVint(201)
        self.writeString(self.player.name)
        self.writeVint(2)
        DataBase.replaceValue(self, 'name', self.player.name)
