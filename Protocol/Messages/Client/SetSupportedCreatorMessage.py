from ByteStream.Reader import Reader
from Protocol.Messages.Server.AvailableServerCommandMessage import AvailableServerCommandMessage
from Protocol.Messages.Server.SetSupportedCreatorResponseMessage import SetSupportedCreatorResponseMessage

class SetSupportedCreatorMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.player.content_creator = self.readString()

    def process(self, db):

        if self.player.content_creator.lower() in self.player.content_creator_codes or self.player.content_creator == '':
            db.update_player_account(self.player.token, 'SupportedContentCreator', self.player.content_creator)
            AvailableServerCommandMessage(self.client, self.player, 215).send()
        else:
            SetSupportedCreatorResponseMessage(self.client, self.player).send()


