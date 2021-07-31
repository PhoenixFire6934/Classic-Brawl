from ByteStream.Reader import Reader
from Protocol.Messages.Server.AllianceResponseMessage import AllianceResponseMessage
from Protocol.Messages.Server.MyAllianceMessage import MyAllianceMessage
from Protocol.Messages.Server.AllianceDataMessage import AllianceDataMessage


class ChangeAllianceSettingsMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.club_id              = self.player.club_id
        self.club_desc            = self.readString()
        self.club_badge           = self.readDataReference()[1]
        self.club_region          = self.readDataReference()[1]
        self.club_type            = self.readVInt()
        self.club_req_trophies    = self.readVInt()
        self.club_family_friendly = self.readVInt()

    def process(self, db):
        db.update_club(self.club_id, 'Description', self.club_desc)
        db.update_club(self.club_id, 'Type', self.club_type)
        db.update_club(self.club_id, 'BadgeID', self.club_badge)
        db.update_club(self.club_id, 'RequiredTrophies', self.club_req_trophies)
        db.update_club(self.club_id, 'FamilyFriendly', self.club_family_friendly)
        db.update_club(self.club_id, 'Region', self.club_region)

        print(self.club_region)

        club_data = db.load_club(self.club_id)

        MyAllianceMessage(self.client, self.player, club_data).send()
        AllianceResponseMessage(self.client, self.player, 10).send()
        AllianceDataMessage(self.client, self.player, club_data).send()