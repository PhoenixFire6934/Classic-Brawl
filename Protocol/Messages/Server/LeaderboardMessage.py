from ByteStream.Writer import Writer

class LeaderboardMessage(Writer):

    def __init__(self, client, player, data):
        super().__init__(client)
        self.id = 24403
        self.player = player
        self.data = data

    def encode(self):
        self.writeVInt(self.player.leaderboard_type)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeString()

        if self.player.leaderboard_type == 1:

            self.writeVInt(len(self.data))

            for entry in self.data:

                self.writeLogicLong(entry['ID'])
                self.writeVInt(1)
                self.writeVInt(entry['Trophies'])

                self.writeVInt(1)
                self.writeString()
                self.writeString(entry['Name'])

                self.writeVInt(9)
                self.writeVInt(28000000 + entry['ProfileIcon'])
                self.writeVInt(43000000 + entry['NameColor'])
                self.writeVInt(0)

            self.writeVInt(0)

            check = False

            for entry in self.data:
                if entry['ID'] == self.player.ID:
                    self.writeVInt(self.data.index(entry) + 1)
                    check = True

            if not check:
                self.writeVInt(0)


        elif self.player.leaderboard_type == 2:
            self.writeVInt(len(self.data))

            for entry in self.data:

                self.writeLogicLong(entry['ID'])
                self.writeVInt(1)
                self.writeVInt(entry['Trophies'])
                self.writeVInt(2)
                self.writeString(entry['Name'])
                self.writeVInt(len(entry['Members']))
                self.writeDataReference(8, entry['BadgeID'])

            self.writeVInt(0)

            check = False

            for x in self.data:
                if x['ID'] == self.player.club_id:
                    self.writeVInt(self.data.index(x) + 1)
                    check = True

            if not check:
                self.writeVInt(0)


        self.writeVInt(0)
        self.writeVInt(0)

        self.writeString(self.player.region)


