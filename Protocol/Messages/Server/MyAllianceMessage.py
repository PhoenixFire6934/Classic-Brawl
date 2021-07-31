from ByteStream.Writer import Writer
from Files.CsvLogic.Regions import Regions

class MyAllianceMessage(Writer):

    def __init__(self, client, player, club_data):
        super().__init__(client)
        self.id = 24399
        self.player = player
        self.club_data   = club_data

    def encode(self):
        if self.club_data['ID'] != 0:

            self.writeVInt(len(self.club_data['Members']))
            self.writeVInt(1)
            self.writeDataReference(25, self.player.club_role)
            self.writeLong(self.club_data['ID'])
            self.writeString(self.club_data['Name'])
            self.writeDataReference(8, self.club_data['BadgeID'])
            self.writeVInt(self.club_data['Type'])
            self.writeVInt(len(self.club_data['Members']))
            self.writeVInt(self.club_data['Trophies'])
            self.writeVInt(self.club_data['RequiredTrophies'])
            self.writeDataReference(0, 0)
            self.writeString(Regions().get_region_string(self.club_data['Region']))
            self.writeVInt(0)
            self.writeVInt(self.club_data['FamilyFriendly'])

        else:
            self.writeVInt(0)
            self.writeVInt(0)

