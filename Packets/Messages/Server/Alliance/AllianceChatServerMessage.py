from Database.DataBase import DataBase
from Utils.Writer import Writer


class AllianceChatServerMessage(Writer):

    def __init__(self, client, player, msg_content):
        super().__init__(client)
        self.msg_content = msg_content
        self.id = 24312
        self.player = player

    def encode(self):
        DataBase.Addmsg(self, 100, 0, self.player.LowID, self.player.name, self.player.ClubRole, self.msg_content)
        DataBase.GetmsgCount(self, self.player.ClubID)

        self.writeVint(2)
        self.writeVint(0)
        self.writeVint(self.player.messageTick)
        self.writeVint(0)
        self.writeVint(self.player.LowID)
        self.writeString(self.player.name)
        self.writeVint(self.player.ClubRole)
        self.writeVint(0)
        self.writeVint(0)
        self.writeString(self.msg_content)