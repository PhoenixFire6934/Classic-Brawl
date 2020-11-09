from Utils.Writer import Writer

class AvatarNameCheckResponseMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 20300
        self.player = player

    def encode(self):
        self.writeVint(0)
        self.writeInt(0)
        self.writeString(self.player.name)
        print("[INFO] Message ChangeNameResponse has been sent.")