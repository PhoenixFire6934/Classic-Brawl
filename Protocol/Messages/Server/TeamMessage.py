from ByteStream.Writer import Writer
from Utils.Helpers import Helpers

class TeamMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24124
        self.player = player

    def encode(self):
        self.writeVInt(1)
        self.writeUInt8(0)
        self.writeVInt(1)
        self.writeLong(Helpers().randomMapID())
        self.writeUInt8(0)
        self.writeUInt8(0)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeDataReference(15, self.player.map_id)

        self.writeVInt(1)
        for x in range(1):

            self.writeVInt(1)

            self.writeLong(self.player.ID)

            self.writeDataReference(16, self.player.home_brawler)
            self.writeDataReference(29, self.player.home_skin)

            self.writeVInt(99999)
            self.writeVInt(99999)
            self.writeVInt(10)

            self.writeVInt(3)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)

            self.writeString(self.player.name)
            self.writeVInt(100)
            self.writeVInt(28000000 + self.player.profile_icon)
            self.writeVInt(43000000 + self.player.name_color)

            self.writeDataReference(23, self.player.starpower) if self.player.starpower != None else self.writeVInt(0)
            self.writeDataReference(23, self.player.gadget)    if self.player.gadget != None else self.writeVInt(0)

        self.writeVInt(0)
        for x in range(0):
            pass

        self.writeVInt(0)
        for x in range(0):
            pass

        self.writeUInt8(0)
        if self.player.use_gadget:
            self.writeUInt8(6)
        else:
            self.writeUInt8(0)
