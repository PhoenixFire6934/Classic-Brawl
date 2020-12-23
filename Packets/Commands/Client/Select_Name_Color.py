from Database.DataBase import DataBase

from Utils.Reader import BSMessageReader

class SelectNameColor(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.namecolor = self.read_Vint()


    def process(self):
        DataBase.replaceValue(self, 'namecolor', self.namecolor)
