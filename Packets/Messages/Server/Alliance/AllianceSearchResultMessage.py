from Utils.Writer import Writer
from Database.DatabaseManager import DataBase
import json


class AllianceSearchResultMessage(Writer):

    def __init__(self, client, player, requestedName, count):
        super().__init__(client)
        self.id = 24310
        self.player = player
        self.requestedName = str(requestedName)
        self.count = count

    def encode(self):
        DataBase.CountClub(self, 1, 100, 2, 30)
        self.writeString(self.requestedName)
        self.writeVint(self.count)

        for i in self.club_list:
            if self.requestedName.lower() in self.club_data[self.club_list.index(i)]['name'].lower():
                DataBase.loadClub(self, i)
                self.writeInt(0)  # ClubHighID
                self.writeInt(i)  # ClubLowID
                self.writeString(self.clubName)  # Club name

                self.writeVint(8)  # BadgeID type
                self.writeVint(self.clubbadgeID)  # Club badge number

                self.writeVint(self.clubtype)  # Club type

                self.writeVint(self.clubmembercount)  # Member count

                self.writeVint(self.clubtrophies)  # Trophies total
                self.writeVint(self.clubtrophiesneeded)  # Trophies needed
                self.writeVint(0)  # Unknown

                self.writeString(self.clubregion)  # Region
                self.writeVint(self.clubmembercount)  # Members online