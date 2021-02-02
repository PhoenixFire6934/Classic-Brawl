from Utils.Writer import Writer


class AllianceBotStreamMessage(Writer):

    def __init__(self, client, player, bot_msg_content):
        super().__init__(client)
        self.bot_msg_content = bot_msg_content
        self.id = 24312
        self.player = player

    def encode(self):
        self.writeVint(2)
        self.writeVint(0)
        self.writeVint(self.player.message_tick)
        self.writeVint(1)
        self.writeVint(1)
        self.writeString("Club Bot")
        self.writeVint(3)
        self.writeVint(0)
        self.writeVint(0)
        self.writeString(self.bot_msg_content)


