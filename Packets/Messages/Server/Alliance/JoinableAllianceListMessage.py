import json
from Utils.Writer import Writer
from Database.DatabaseManager import DataBase


class JoinableAllianceListMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24304
        self.player = player

    def encode(self):
        DataBase.CountClub(self, 1, 100, 2, 50)

        self.writeVint(self.AllianceCount)

        for i in self.club_list:
            DataBase.loadClub(self, i)
            self.writeInt(0)                                 # ClubHighID
            self.writeInt(i)                                 # ClubLowID
            self.writeString(self.clubName)                  # Club name

            self.writeVint(8)                                # BadgeID type
            self.writeVint(self.clubbadgeID)                 # Club badge number

            self.writeVint(self.clubtype)                    # Club type

            self.writeVint(self.clubmembercount)             # Member count

            self.writeVint(self.clubtrophies)                # Trophies total
            self.writeVint(self.clubtrophiesneeded)          # Trophies needed
            self.writeVint(0)                                # Unknown

            self.writeString(self.clubregion)                # Region
            self.writeVint(self.clubmembercount)             # Members online