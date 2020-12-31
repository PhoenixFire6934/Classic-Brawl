from os import truncate
from Utils.Writer import Writer
from Database.DataBase import DataBase


class PlayerProfileMessage(Writer):

    def __init__(self, client, player, high_id, low_id):
        super().__init__(client)
        self.id = 24113
        self.player = player
        self.high_id = high_id
        self.low_id = low_id

    def encode(self):
        self.writeVint(self.high_id)  # High Id
        self.writeVint(self.low_id)  # Low Id
        self.writeVint(0) # Unknown

        DataBase.loadOtherAccount(self, self.low_id)

        self.writeVint(len(self.BrawlersCount))  # Brawlers array

        for brawler_id in self.BrawlersCount:
            self.writeScId(16, brawler_id)
            self.writeVint(0)
            self.writeVint(99999)
            self.writeVint(99999)
            self.writeVint(10) # power lvl


        self.writeVint(15)

        self.writeVint(1)
        self.writeVint(99999)  # 3v3 victories

        self.writeVint(2)
        self.writeVint(99999) # Player experience

        self.writeVint(3)
        self.writeVint(self.trophies) # Trophies

        self.writeVint(4)
        self.writeVint(self.maxTrophiesReached)  # Highest trophies

        self.writeVint(5)
        self.writeVint(len(self.BrawlersCount)) # Brawlers list
        
        self.writeVint(7)
        self.writeVint(28000000 + self.profileIcon) # Profile icon??

        self.writeVint(8)
        self.writeVint(99999)  # Solo victories

        self.writeVint(9)
        self.writeVint(99999) # Best robo rumble time

        self.writeVint(10)
        self.writeVint(99999) # Best time as big brawler

        self.writeVint(11)
        self.writeVint(99999)  # Duo victories

        self.writeVint(12)
        self.writeVint(21) # Highest boss fight lvl passed

        self.writeVint(13)
        self.writeVint(10) # Unknown

        self.writeVint(14)
        self.writeVint(1) # Highest power play rank

        self.writeVint(15)
        self.writeVint(99999)  # most challenge wins

        self.writeVint(16)
        self.writeVint(20)

        self.writeString(self.name)
        self.writeVint(1)
        self.writeVint(28000000 + self.profileIcon) # Profile icon
        self.writeVint(43000000 + self.namecolor) # Name color

        if self.ClubID != 0:
            DataBase.loadClub(self, self.ClubID)

            self.writeBoolean(True)

            self.writeInt(0)
            self.writeInt(self.ClubID)
            self.writeString(self.clubName) # club name
            self.writeVint(8)
            self.writeVint(self.clubbadgeID) # Club badgeID
            self.writeVint(self.clubtype) # club type | 1 = Open, 2 = invite only, 3 = closed
            self.writeVint(self.clubmembercount) # Current members count
            self.writeVint(self.clubtrophies)
            self.writeVint(self.clubtrophiesneeded) # Trophy required
            self.writeVint(0) # (Unknown)
            self.writeString(self.clubregion) # region
            self.writeVint(0) # (Unknown)
            self.writeVint(0) # (Unknown)
            self.writeVint(19)
            self.writeVint(self.ClubRole)
        else:
            self.writeVint(0)
            self.writeVint(0)