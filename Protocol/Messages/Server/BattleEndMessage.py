from ByteStream.Writer import Writer


class BattleEndMessage(Writer):

    def __init__(self, client, player, type, result, players):
        super().__init__(client)
        self.id = 23456
        self.player  = player
        self.type    = type
        self.result  = result
        self.players = players

    def encode(self):
        self.writeVInt(self.type)
        self.writeVInt(self.result)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(1)

        self.writeVInt(0)
        self.writeVInt(32)
        self.writeVInt(0)
        self.writeVInt(1)

        self.writeVInt(len(self.players))

        for player in self.players:
            self.brawler  = self.players[player]['Brawler']
            self.skin     = self.players[player]['Skin']
            self.team     = self.players[player]['Team']
            self.username = self.players[player]['Name']

            if self.type == 5:
                if self.team == 0:
                    self.writeVInt(player)
                else:
                    self.writeVInt(2)

            elif self.type == 2:
                if self.team != 0:
                    self.writeVInt(2 if self.team != 0 else 1)

            else:
               self.writeVInt(self.team if self.team != 1 else 2)

            self.writeDataReference(16, self.brawler)if self.brawler != -1 else self.writeVInt(0)
            self.writeDataReference(29, self.skin)   if self.skin != -1 else self.writeVInt(0)

            self.writeVInt(99999)
            self.writeVInt(99999)
            self.writeVInt(10)

            self.writeBool(False)

            # sub_64DF74
            self.writeString(self.username)
            self.writeVInt(100)
            self.writeVInt(28000000)
            self.writeVInt(43000000)

        self.writeBool(False)
        self.writeBool(False)
        self.writeBool(False)

        self.writeDataReference(28, 0)

        self.writeBool(False)