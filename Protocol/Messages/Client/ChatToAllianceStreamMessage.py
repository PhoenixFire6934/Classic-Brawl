from ByteStream.Reader import Reader
from Protocol.Messages.Server.AllianceStreamMessage import AllianceStreamMessage

class ChatToAllianceStreamMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.msg = self.readString()

    def process(self, db):
        club_data = db.load_club(self.player.club_id)

        self.player.message_tick = club_data['Messages'][-1]['Tick'] if club_data['Messages'] else self.player.message_tick
        self.player.message_tick += 1

        message = {'Event': 2 ,'Message': self.msg, 'PlayerID': self.player.ID, 'PlayerName':self.player.name, 'PlayerRole':self.player.club_role, 'Tick': self.player.message_tick}

        club_data['Messages'].append(message)
        db.update_club(self.player.club_id, 'Messages', club_data['Messages'])

        for member in club_data['Members']:
            member_id = member['ID']
            AllianceStreamMessage(self.client, self.player, [message]).sendByID(member_id)