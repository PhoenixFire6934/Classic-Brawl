from Utils.Writer import Writer
from Database.DataBase import DataBase
import random

class TeamGameroomDataMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24124
        self.player = player

    def encode(self):
        self.writeVint(1)
        self.writeVint(0)
        self.writeVint(1)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        if (self.player.room_id == 0):
            self.player.room_id = random.randint(0, 2147483647)
            self.writeInt(self.player.room_id)
            DataBase.replaceValue(self, 'roomID', self.player.room_id)
        else:
           self.writeInt(self.player.room_id)

        self.writeVint(1557129593)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeScId(15, self.player.map_id)

        self.writeVint(1)
        self.writeVint(1)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)  # High Id
        self.writeInt(1)   # Low Id

        self.writeScId(16, self.player.brawler_id)

        self.writeVint(0)

        self.writeVint(99999)
        self.writeVint(99999)

        self.writeVint(1)
        self.writeVint(3)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeString(self.player.name)

        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)

        self.writeScId(23, self.player.starpower)

        if self.player.use_gadget == 1:
            self.writeScId(23, self.player.gadget)
        else:
           self.writeVint(0)
           self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(6)


