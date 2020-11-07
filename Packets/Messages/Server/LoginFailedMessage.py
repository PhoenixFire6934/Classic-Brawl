from Utils.Writer import Writer


class LoginFailed(Writer):

    def __init__(self, client, player, msg):
        super().__init__(client)
        self.id = 20103
        self.player = player
        self.msg = msg

    def encode(self):
        self.writeInt(self.player.err_code) # error code
        self.writeString() # fingerprint

        self.writeString() # null

        self.writeString() # patch url
        self.writeString(self.player.updateUrl) # update url
        self.writeString(self.msg) # message

        self.writeHexa('''00 00 00 00 00 FF FF FF FF 00 00 00 02''') # unknown

        self.writeString() # patch url
        self.writeString() # rackcdn url

        self.writeInt(0)
        self.writeInt(0) # time left ?

        self.writeString() # null
        self.writeString() # null

        self.writeHexa('''02 00 00 00 00 00 00 00 00 00''') # unknown

        print("[INFO] Message LoginFailed has been sent.")
