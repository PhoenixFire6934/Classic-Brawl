from ByteStream.Writer import Writer


class LoginOkMessage(Writer):
    def __init__(self, client, player, account_id, account_token):
        super().__init__(client)
        self.player = player
        self.account_id = account_id
        self.account_token = account_token
        self.id = 20104

    def encode(self):
        self.writeLong(self.account_id)
        self.writeLong(self.account_id)

        self.writeString(self.account_token)
        self.writeString()
        self.writeString()

        self.writeInt(26)
        self.writeInt(184)
        self.writeInt(1)

        self.writeString("dev")

        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)

        self.writeString()
        self.writeString()
        self.writeString()

        self.writeInt(0)

        self.writeString()
        self.writeString(self.player.region)
        self.writeString()

        self.writeInt(1)
        self.writeString()

        self.writeInt(2)
        self.writeString()
        self.writeString()

        self.writeInt(1)
        self.writeString()

