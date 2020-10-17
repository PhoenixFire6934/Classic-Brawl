from Utils.Writer import Writer


class OutOfSync(Writer):

    def __init__(self, client, player, message):
        super().__init__(client)
        self.id = 20103
        self.player = player
        self.msg = message

    def encode(self):
        self.writeInt(3)
        self.writeString()
        self.writeString()
        self.writeString()
        self.writeString("")
        self.writeString(self.msg)
        self.writeHexa('''2E0000012C000000000000000000''')
        self.writeString()
        self.writeString()
        self.writeString()
        self.writeString()
        self.writeHexa('''00FFFF0000000000''')
        print("[INFO] Message LoginFailed has been sent.")