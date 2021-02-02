from Utils.Writer import Writer
from Database.DatabaseManager import DataBase


class AllianceBotChatServerMessage(Writer):

    def __init__(self, client, player, bot_msg_content):
        super().__init__(client)
        self.bot_msg_content = bot_msg_content
        self.id = 24312
        self.player = player

    def encode(self):
        DataBase.GetmsgCount(self, self.player.club_low_id)
        self.writeVint(2)
        self.writeVint(0)
        self.writeVint(self.MessageCount)
        self.writeVint(1)
        self.writeVint(1)
        self.writeString("Club Bot")
        self.writeVint(3)
        self.writeVint(0)
        self.writeVint(0)
        self.writeString(self.bot_msg_content)


