from Packets.Commands.Server.Change_Name_Callback import ChangeNameCallback
from Packets.Messages.Server.Home.Avatar_Name_Change_Failed_Message import AvatarNameChangeFailedMessage

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
                ChangeNameCallback(self.client, self.player, self.state).send()
            else:
                AvatarNameChangeFailedMessage(self.client, self.player).send()
        else:
            AvatarNameChangeFailedMessage(self.client, self.player).send()
