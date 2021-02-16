from Database.DatabaseManager import DataBase
from Utils.Writer import Writer


class MyAllianceMessage(Writer):

    def __init__(self, client, player, LowID):
        super().__init__(client)
        self.id = 24399
        self.player = player
        self.clubid = LowID

    def encode(self):
        if self.clubid != 0:
            DataBase.loadClub(self, self.clubid)
            self.writeVint(self.clubmembercount)
            self.writeVint(1)
            self.writeVint(25)

            self.writeVint(self.player.club_role)

            # Club info
            self.writeInt(0)                            # Club high id
            self.writeInt(self.clubid)               # Club low id
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

            self.writeVint(0)
            self.writeString(self.clubregion)           # Region
            
            self.writeVint(0)
            self.writeVint(self.clubfriendlyfamily)     # Family friendly status | 0 = Can be activated, 1 = Activated  

        else:
            self.writeVint(0)
            self.writeVint(0)