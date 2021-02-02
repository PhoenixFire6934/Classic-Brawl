from Packets.Messages.Server.Login.LoginFailedMessage import LoginFailedMessage

from Utils.Reader import BSMessageReader

class ClientHelloMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        pass

    def process(self):
        self.player.err_code = 8
        LoginFailedMessage(self.client, self.player, "The server does not support your version").send()