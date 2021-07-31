from ByteStream.Writer import Writer

class LogicChangeAvatarNameCommand(Writer):

    def encode(self):
        self.writeString(self.player.name)
        self.writeVInt(1)