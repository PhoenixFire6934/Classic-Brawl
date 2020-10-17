from Utils.Writer import Writer


class ClubProfileMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24301
        self.player = player

    def encode(self):
        self.writeVint(0)
        self.writeInt(0)
        self.writeInt(521)
        self.writeString("<cff2400>V<cff4800>i<cff6d00>t<cfe9100>a<cffb600>l<cffda00>i<cfffe00>k<cffff00>O<cdaff00>b<cb6ff00>j<c91ff00>e<c6dfe00>c<c48ff00>t</c> <c4>and</c> <cff002a>P<cff0054>h<cff007f>o<cff00a9>e<cff00d4>n<cfe00fe>i<cff00ff>x<cd400ff>F<caa00ff>i<c7f00ff>r<c5500ff>e</c>")
        self.writeVint(8)
        self.writeVint(11)
        self.writeVint(3)
        self.writeVint(1)
        self.writeVint(9999)
        self.writeVint(0)
        self.writeVint(0)
        self.writeString("IL")
        self.writeVint(0)
        self.writeString("Welcome!")
        self.writeVint(1)
        self.writeInt(3182494701)
        self.writeInt(2935259141)
        self.writeVint(7)
        self.writeString("<cff3200>M<cff6500>r<cff9800> <cffcb00>V<cffff00>i<cccff00>t<c99ff00>a<c66ff00>l<c33ff00>i<c01ff00>k</c>")
        self.writeVint(7)
        self.writeVint(2)
        self.writeVint(0)
        self.writeVint(9999)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(28)
        self.writeVint(33)
        self.writeVint(0)
        print("[INFO] Message ClubProfileMessage has been sent.")