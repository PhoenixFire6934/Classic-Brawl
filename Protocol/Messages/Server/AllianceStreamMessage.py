from ByteStream.Writer import Writer

class AllianceStreamMessage(Writer):

    def __init__(self, client, player, msg):
        super().__init__(client)
        self.id = 24311
        self.player = player
        self.msg = msg


    def encode(self):
        if self.player.club_id != 0:
            self.writeVInt(len(self.msg))
            for x in self.msg:
                print(x)
                self.writeVInt(x['Event'])
                self.writeVInt(0)
                self.writeVInt(x['Tick'])
                self.writeLogicLong(x['PlayerID'])
                self.writeString(x['PlayerName'])
                self.writeVInt(x['PlayerRole'])
                self.writeVInt(0)
                self.writeVInt(0)

                if x['Event'] == 4:
                    self.writeVInt(x['Message'])
                    self.writeVInt(1)
                    self.writeVInt(0)
                    self.writeLogicLong(x['PlayerID'])
                    self.writeString(x['PlayerName'])

                else:
                    self.writeString(x['Message'])
        else:
            self.writeVInt(0)

