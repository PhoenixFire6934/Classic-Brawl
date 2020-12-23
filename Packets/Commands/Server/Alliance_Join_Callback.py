from os import write
from Utils.Writer import Writer
from Database.DataBase import DataBase
import json


class AllianceJoinCallback(Writer):

    def __init__(self, client, player, clubid):
        super().__init__(client)
        self.id = 24111
        self.player = player
        self.clubid = clubid

    def encode(self):
        DataBase.loadOwnClub(self, self.clubid)

        self.writeVint(1)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeInt(self.clubid)
        self.writeString(self.clubName) # club name
        self.writeVint(8)
        self.writeVint(self.clubbadgeID) # Club badgeID
        self.writeVint(self.clubtype) # club type | 1 = Open, 2 = invite only, 3 = closed
        self.writeVint(self.clubmembercount) # Current members count
        self.writeVint(self.clubtrophies)
        self.writeVint(self.clubtrophiesneeded) # Trophy required
        self.writeVint(0)
        self.writeString(self.clubregion) # region
        self.writeVint(0)
        self.writeVint(self.clubfriendlyfamily) # Family friendly status | 0 = Can be activated, 1 = Activated
        self.writeString(self.clubdescription) # Description
        self.writeVint(self.clubmembercount) # Members
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0) # High Id
        self.writeInt(self.player.LowID)  # Low Id
        self.writeVint(2) # player club role | 0 = Nothing, 1 = Member, 2 = President, 3 = Senior, 4 = Vice President
        self.writeVint(self.player.trophies)
        self.writeVint(0) # states
        self.writeVint(0)
        self.writeVint(0)
        self.writeString(self.player.name)
        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)
