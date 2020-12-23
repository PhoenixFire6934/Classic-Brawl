from Database.DataBase import DataBase
from Utils.Writer import Writer


class BotProfileMessage(Writer):

    def __init__(self, client, player, low_id):
        super().__init__(client)
        self.id = 24113
        self.player = player
        self.low_id = low_id

    def encode(self):
        DataBase.loadOtherAccount(self, self.low_id)
        self.writeVint(1)  # High Id
        self.writeVint(self.low_id)  # Low Id
        self.writeVint(0)

        self.writeVint(len(self.player.BrawlersCount))  # brawlers array

        for brawler_id in self.player.BrawlersCount:
            self.writeScId(16, brawler_id)
            self.writeVint(0)
            self.writeVint(99999)
            self.writeVint(99999)
            self.writeVint(10) # power lvl


        self.writeVint(15)

        self.writeVint(1)
        self.writeVint(99999)  # 3v3 victories

        self.writeVint(2)
        self.writeVint(1262470) # Player experience

        self.writeVint(3)
        self.writeVint(99999)

        self.writeVint(4)
        self.writeVint(self.trophies)  # Highest trophies

        self.writeVint(5)
        self.writeVint(len(self.player.BrawlersCount))

        self.writeVint(7)
        self.writeVint(self.profileIcon + 28000000) # Profile icon??

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
        self.writeVint(10)

        self.writeVint(14)
        self.writeVint(1) # Highest power play rank

        self.writeVint(15)
        self.writeVint(99999)  # most challenge wins

        self.writeVint(16)
        self.writeVint(21)

        self.writeString(self.name)
        self.writeVint(100)
        self.writeVint(self.profileIcon + 28000000)
        self.writeVint(self.namecolor + 43000000)

        if self.player.ClubID != 0:
            DataBase.loadClub(self, self.ClubID, 1)
            self.writeVint(1)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
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
            self.writeVint(1)
        else:
            self.writeVint(0)
            self.writeVint(0)