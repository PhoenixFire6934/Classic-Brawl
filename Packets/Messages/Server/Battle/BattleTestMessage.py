from Utils.Writer import Writer
from Database.DatabaseManager import DataBase


class BattleTestMessage(Writer):

    def __init__(self, client, player, state):
        super().__init__(client)
        self.id = 20405
        self.player = player
        self.state = state

    def encode(self):
        self.writeInt(0) # timer
        self.writeInt(1)  # Current player
        self.writeInt(self.player.mmplayers) # Max player

        self.writeInt(1)  # Unknown
        self.writeString("Player")
        self.writeVint(10)

        