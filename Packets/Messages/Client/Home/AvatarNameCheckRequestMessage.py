from Packets.Commands.Server.LogicChangeAvatarNameCommand import LogicChangeAvatarNameCommand

from Utils.Reader import BSMessageReader


class AvatarNameCheckRequestMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.player.name = self.read_string()

    def process(self):
        LogicChangeAvatarNameCommand(self.client, self.player, 1).send()