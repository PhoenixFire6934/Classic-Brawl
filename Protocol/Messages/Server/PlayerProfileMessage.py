from ByteStream.Writer import Writer
from Files.CsvLogic.Regions import Regions
from Logic.Avatar.LogicPlayerStats import LogicPlayerStats


class PlayerProfileMessage(Writer):

    def __init__(self, client, player, player_data, db):
        super().__init__(client)
        self.id = 24113
        self.player = player
        self.player_data = player_data
        self.db = db

    def encode(self):
        self.writeLogicLong(self.player_data['ID'])

        self.writeDataReference(0, 0)

        self.writeVInt(len(self.player_data['UnlockedBrawlers']))
        for x in self.player_data['UnlockedBrawlers']:
            # HeroEntry::encode
            self.writeDataReference(16, x)
            self.writeDataReference(0, 0)
            self.writeVInt(self.player_data['BrawlersTrophies'][str(x)])
            self.writeVInt(self.player_data['BrawlersHighestTrophies'][str(x)])
            self.writeVInt(self.player_data['BrawlersLevel'][str(x)] + 2)

        self.playerStats = LogicPlayerStats.getPlayerStats(self, self.player_data)

        self.writeVInt(len(self.playerStats))
        for x in self.playerStats:
            self.writeVInt(list(self.playerStats.keys()).index(x) + 1)
            self.writeVInt(self.playerStats[x])

        # PlayerDisplayData::encode
        self.writeString(self.player_data['Name'])
        self.writeVInt(100) # Unknown
        self.writeVInt(28000000 + self.player_data['ProfileIcon'])
        self.writeVInt(43000000 + self.player_data['NameColor'])

        if self.player_data['ClubID'] != 0:
            club_data = self.db.load_club(self.player_data['ClubID'])

            self.writeBoolean(True)
            self.writeLong(club_data['ID'])
            self.writeString(club_data['Name'])
            self.writeDataReference(8, club_data['BadgeID'])
            self.writeVInt(club_data['Type'])
            self.writeVInt(len(club_data['Members']))
            self.writeVInt(club_data['Trophies'])
            self.writeVInt(club_data['RequiredTrophies'])
            self.writeDataReference(0, 0)
            self.writeString(Regions().get_region_string(club_data['Region']))
            self.writeVInt(0)
            self.writeUInt8(0)
            self.writeDataReference(25, self.player_data['ClubRole'])

        else:
            self.writeBoolean(False)
            self.writeVInt(0)