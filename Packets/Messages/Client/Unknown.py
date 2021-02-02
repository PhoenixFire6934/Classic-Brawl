from Utils.ColorCode import bcolors

from Utils.Reader import BSMessageReader


class Unknown1(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        list = []
        for i in range(30):
            list.append(self.read_Vint())
        print(f'{bcolors.FAIL} {list} {bcolors.ENDC}')

    def process(self):
        pass
        #UnknownServerPackets(self.client, self.player).send()
        #KeepAliveOkMessage(self.client, self.player).send()