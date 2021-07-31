from ByteStream.Reader import Reader
from Protocol.Messages.Server.AllianceResponseMessage import AllianceResponseMessage
from Protocol.Messages.Server.MyAllianceMessage import MyAllianceMessage


class LeaveAllianceMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        pass

    def process(self, db):
        club_data = db.load_club(self.player.club_id)

        if len(club_data['Members']) == 1:
            db.delete_club(self.player.club_id)
        else:
            for member in club_data['Members']:
                if member['ID'] == self.player.ID:
                    del club_data['Members'][club_data['Members'].index(member)]
                    db.update_club(self.player.club_id, 'Members', club_data['Members'] )

        self.player.club_id = 0
        db.update_player_account(self.player.token, 'ClubID', 0)

        AllianceResponseMessage(self.client, self.player, 80).send()
        MyAllianceMessage(self.client, self.player, {'ID':0}).send()