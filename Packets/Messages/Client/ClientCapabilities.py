from Utils.Reader import BSMessageReader


class ClientCapabilities(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)

    def decode(self):
        self.Latency = self.read_Vint()

    def process(self):
        pass