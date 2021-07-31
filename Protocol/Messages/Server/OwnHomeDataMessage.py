from Logic.ClientHome import LogicClientHome
from Logic.ClientAvatar import LogicClientAvatar
from ByteStream.Writer import Writer
from datetime import datetime

class OwnHomeDataMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24101
        self.player = player
        self.time_stamp = int(datetime.timestamp(datetime.now()))

    def encode(self):

        LogicClientHome.encode(self)
        LogicClientAvatar.encode(self)

        self.writeVInt(self.time_stamp)

