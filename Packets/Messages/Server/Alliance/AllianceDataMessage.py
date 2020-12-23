from Logic.Player import Players
from os import SEEK_CUR, curdir
from Database.DataBase import DataBase
from Utils.Writer import Writer
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
        
        if self.player.ClubID == self.clubLowID:
            self.writeVint(0)
        else:
            self.writeVint(0)

        # ClubID
        self.writeInt(0)                            # Club high id
        self.writeInt(self.clubLowID)               # Club low id

        self.writeString(self.clubName)             # Club name

        # Badge
        self.writeVint(8)
        self.writeVint(self.clubbadgeID)            # Club badge id

        # Club settings
        self.writeVint(self.clubtype)               # Club type
        self.writeVint(self.clubmembercount)        # Club members count

        # Club trophies
        self.writeVint(self.clubtrophies)           # Club total trophies
        self.writeVint(self.clubtrophiesneeded)     # Club required trophies

        # Club Info
        self.writeVint(0)
        self.writeString(self.clubregion)           # Region
        self.writeVint(0)
        self.writeVint(self.clubfriendlyfamily)     # Family friendly status | 0 = Can be activated, 1 = Activated

        self.writeString(self.clubdescription)      # Description

        # Members list
        self.writeVint(self.clubmembercount)        # Members list length

        for id in range(len(self.plrids)):
            DataBase.GetMemberData(self, self.plrids[id])

            if self.plrname == self.player.name:
                self.writeInt(0)
            else:
                self.writeInt(1)                                # High Id

            self.writeInt(self.plrids[id])                      # Low Id

            self.writeVint(self.plrrole)                        # player club role | 0 = Nothing, 1 = Member, 2 = President, 3 = Senior, 4 = Vice President
            self.writeVint(self.plrtrophies)                    # trophies
            self.writeVint(2)                                   # Player states | 0 = last online 1 hour ago, 1 = battling, 2 = menu, 4 = matchmaking, 6 = last online 1 month ago, 7 = spectating, 8 = practicing
            self.writeVint(0)
            self.writeVint(0)
            self.writeString(self.plrname)
            self.writeVint(1)
            self.writeVint(28000000 + self.plricon)
            self.writeVint(43000000 + self.plrnamecolor)