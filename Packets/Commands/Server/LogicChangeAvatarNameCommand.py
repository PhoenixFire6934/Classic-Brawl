from Utils.Writer import Writer
from Database.DataBase import DataBase

class LogicChangeAvatarNameCommand(Writer):

    def __init__(self, client, player, state):
        super().__init__(client)
        self.id = 24111
        self.player = player
        self.state = state

    def encode(self):
        self.writeVint(201)
        self.writeString(self.player.name)
        self.writeVint(self.state)

        DataBase.replaceValue(self, 'name', self.player.name)
