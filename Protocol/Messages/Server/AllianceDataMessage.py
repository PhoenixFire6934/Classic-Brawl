from ByteStream.Writer import Writer
from Files.CsvLogic.Regions import Regions

class AllianceDataMessage(Writer):

    def __init__(self, client, player, club_data):
        super().__init__(client)
        self.id = 24301
        self.player = player
        self.club_data = club_data

    def encode(self):
        if self.club_data['ID'] != 0:

            self.writeVInt(0)
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

            self.writeString(self.club_data['Description'])

            self.writeVInt(len(self.club_data['Members']))

            for member in self.club_data['Members']:
                self.writeLong(member['ID'])
                self.writeVInt(member['Role'])
                self.writeVInt(member['Trophies'])
                self.writeVInt(2) # Player Status
                self.writeVInt(0)
                self.writeVInt(0)

                self.writeString(member['Name'])
                self.writeVInt(100)
                self.writeVInt(28000000 + member['ProfileIcon'])
                self.writeVInt(43000000 + member['NameColor'])

        else:
            self.writeVInt(2)



