from Utils.Writer import Writer


class KeepAliveOk(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 20108
        self.player = player

    def encode(self):
        print("[INFO] Message KeepAliveOk has been sent.")