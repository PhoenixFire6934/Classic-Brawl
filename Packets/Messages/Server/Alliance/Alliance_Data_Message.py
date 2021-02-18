from Logic.Player import Players
from os import SEEK_CUR, curdir
from Utils.Writer import Writer
from Database.DatabaseManager import DataBase
import json


class AllianceDataMessage(Writer):

    def __init__(self, client, player, clubHighID, clubLowID):
        super().__init__(client)
        self.id = 24301
        self.player = player
        self.clubHighID = clubHighID
        self.clubLowID = clubLowID

    def encode(self):
        DataBase.loadClub(self, self.clubLowID)

        if self.player.club_low_id == 0:
            self.writeVint(0)
        else:
            self.writeVint(1)

        # ClubID
        self.writeInt(0)                            # Club high id
        self.writeInt(self.clubLowID)               # Club low id

        self.writeString(self.clubName)             # Club name

        # Badge
        self.writeVint(8)
        self.writeVint(self.clubbadgeID)            # Club badge id

        # Club settings
        self.writeVint(self.clubtype)               # Club type [1 = open, 2 = invite only, 3 = closed]
        self.writeVint(len(self.plrids))        # Club members count

        # Club trophies
        self.writeVint(self.clubtrophies)           # Club total trophies
        self.writeVint(self.clubtrophiesneeded)     # Club required trophies

        # Club Info
        self.writeVint(0)
        self.writeString(self.clubregion)           # Region
        self.writeVint(0)
        self.writeString(self.clubdescription)      # Description

        # Members list
        self.writeVint(len(self.plrids))        # Members list count

        for id in self.plrids:
            DataBase.GetMemberData(self, id)

            self.writeInt(0)  # High Id
            self.writeInt(id) # Low Id
            self.writeString(self.plrname)

            self.writeVint(self.plrrole)                        # player club role | 0 = Nothing, 1 = Member, 2 = President, 3 = Senior, 4 = Vice President
            self.writeVint(0)
            self.writeVint(self.plrtrophies)                    # trophies
            self.writeVint(2)                                   # Player states | 0 = last online 1 hour ago, 1 = battling, 2 = menu, 4 = matchmaking, 6 = last online 1 month ago, 7 = spectating, 8 = practicing
            self.writeVint(0)
            self.writeScId(28, self.plricon)