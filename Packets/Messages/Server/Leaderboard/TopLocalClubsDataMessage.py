from Utils.Writer import Writer
from Database.DatabaseManager import DataBase


class GetLeaderboardClubLocalOkMessage(Writer):

    def __init__(self, client, player, type):
        super().__init__(client)
        self.id = 24403
        self.player = player
        self.type = type

    def encode(self):
        self.indexOfClub = 0
        self.writeVint(2)
        self.writeVint(0) # SCID
        self.writeString(self.player.region) # Player Region

        DataBase.CountClub(self, 1, 100, 2, 200)

        def by_trophy(club):
            print(club)
            return club['trophies']

        self.writeVint(self.AllianceCount)
        self.club_data.sort(key=by_trophy, reverse=True)

        for club in self.club_data:
            if club["clubID"] == self.player.club_low_id:
                self.indexOfClub = self.club_data.index(club) + 1
            DataBase.loadClub(self, club['clubID'])
            self.writeVint(0)  # Club High ID
            self.writeVint(club['clubID'])  # Club Low ID

            self.writeVint(1)
            self.writeVint(self.clubtrophies)  # Club Trophies
            self.writeVint(2)

            self.writeString(self.clubName)  # Club Name
            self.writeVint(self.clubmembercount)  # Club Members Count

            self.writeVint(8)  # Club Badge
            self.writeVint(self.clubbadgeID)  # Club Name Color


        self.writeVint(0)
        self.writeVint(self.indexOfClub) # Index of the club
        self.writeVint(0)
        self.writeVint(0)
        self.writeString(self.player.region)