from ByteStream.Reader import Reader
from Protocol.Messages.Server.AllianceResponseMessage import AllianceResponseMessage
from Protocol.Messages.Server.MyAllianceMessage import MyAllianceMessage
from Protocol.Messages.Server.AllianceStreamMessage import AllianceStreamMessage

class JoinAllianceMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.club_id = self.readLong()

    def process(self, db):
        self.player.club_id = self.club_id
        self.player.club_role = 1

        club_data = db.load_club(self.club_id)
        club_data['Members'].append(
            {
                f'Name': self.player.name,
                'ID': self.player.ID,
                'Role': self.player.club_role,
                'Trophies': self.player.trophies,
                'ProfileIcon': self.player.profile_icon,
                'NameColor': self.player.name_color
            }
        )

        db.update_club(self.club_id, 'Members', club_data['Members'])
        db.update_club(self.club_id, 'Trophies', club_data['Trophies'] + self.player.trophies)
        db.update_player_account(self.player.token, 'ClubID', self.player.club_id)
        db.update_player_account(self.player.token, 'ClubRole', self.player.club_role)

        AllianceResponseMessage(self.client, self.player, 40).send()
        MyAllianceMessage(self.client, self.player, club_data).send()
        AllianceStreamMessage(self.client, self.player, club_data['Messages']).send()
