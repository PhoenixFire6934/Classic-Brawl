from ByteStream.Reader import Reader
from Protocol.Messages.Server.AvailableServerCommandMessage import AvailableServerCommandMessage
from Protocol.Messages.Server.AvatarNameChangeFailedMessage import AvatarNameChangeFailedMessage

class SetNameMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.username = self.readString()
        self.state = self.readVInt()

    def process(self, db):
        if self.username != '':
            if len(self.username) >= 2 and len(self.username) <= 20:
                self.player.name = self.username
                db.update_player_account(self.player.token, 'Name', self.username)
                db.update_player_account(self.player.token, 'NameSet', True)
                AvailableServerCommandMessage(self.client, self.player, 201).send()
            else:
                AvatarNameChangeFailedMessage(self.client, self.player).send()
        else:
            AvatarNameChangeFailedMessage(self.client, self.player).send()