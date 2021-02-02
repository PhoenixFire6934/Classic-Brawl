from Packets.Commands.Server.LogicChangeAvatarNameCommand import LogicChangeAvatarNameCommand
from Packets.Messages.Server.Home.AvatarNameChangeFailedMessage import AvatarNameChangeFailedMessage

from Utils.Reader import BSMessageReader


class SetNameMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.username = self.read_string()
        self.state = self.read_Vint()

    def process(self):
        if self.username != '':
            if len(self.username) >= 2 and len(self.username) <= 20:
                self.player.name = self.username
                LogicChangeAvatarNameCommand(self.client, self.player, self.state).send()
            else:
                AvatarNameChangeFailedMessage(self.client, self.player).send()
        else:
            AvatarNameChangeFailedMessage(self.client, self.player).send()
