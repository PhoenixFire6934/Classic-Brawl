from Utils.Writer import Writer

class SetContentCreatorResponse(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24111
        self.player = player

    def encode(self):
        print("sended too", self.player.contentCreator)
        self.writeVint(208)
        self.writeString(self.player.contentCreator)
        self.writeVint(0)
        self.writeVint(1)
        self.writeVint(-1)
        self.writeVint(-1)
        self.writeVint(0)
        self.writeVint(0)
        print("sended too", self.player.contentCreator)