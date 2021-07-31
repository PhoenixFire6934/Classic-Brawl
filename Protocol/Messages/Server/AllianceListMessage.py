from ByteStream.Writer import Writer
from Files.CsvLogic.Regions import Regions

class AllianceListMessage(Writer):

    def __init__(self, client, player, query, clubs):
        super().__init__(client)
        self.id = 24310
        self.player = player
        self.query = query
        self.clubs = clubs

    def encode(self):

        self.writeString(self.query)

        self.writeVInt(len(self.clubs))

        for club in self.clubs:
            self.writeLong(club['ID'])
            self.writeString(club['Name'])
            self.writeDataReference(8, club['BadgeID'])
            self.writeVInt(club['Type'])
            self.writeVInt(len(club['Members']))
            self.writeVInt(club['Trophies'])
            self.writeVInt(club['RequiredTrophies'])
            self.writeDataReference(0,0)
            self.writeString(Regions().get_region_string(club['Region']))
            self.writeVInt(0)
            self.writeVInt(club['FamilyFriendly'])