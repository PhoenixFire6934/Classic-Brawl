from Utils.Writer import Writer


class BattleLogMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 23458
        self.player = player

    def encode(self):
        self.writeBoolean(True)

        self.writeVint(0) # Count

        self.writeVint(0)
        self.writeVint(0)    # Time When Battle Log Entry Was Created
        self.writeVint(1)    # Battle Log Type (1 = Normal, 2 = Crash, 3 = Survived for <time>, 
        self.writeVint(6)    # Trophies Result
        self.writeVint(120)  # Battle Time
        self.writeUInt8(0)   # Type [0 = Power Play, 1 = Friendly, 2 = Championship]
        self.writeScId(15, 95) # Map SCID
        self.writeVint(2) # Victory/Defeat/Draw
        self.writeVint(0) # ???

        self.writeInt(0)
        self.writeInt(0)

        self.writeVint(1)
        self.writeUInt8(1)

        self.writeVint(0)  # array

        self.writeVint(0)
        self.writeUInt8(0)
        self.writeVint(0)
        self.writeUInt8(0)
        self.writeVint(0)

        print("[INFO] Message BattleLogMessage has been sent.")
