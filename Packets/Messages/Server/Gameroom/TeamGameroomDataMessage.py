from Utils.Writer import Writer
from Database.DatabaseManager import DataBase

class TeamGameroomDataMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24124
        self.player = player

    def encode(self):
        DataBase.loadGameroom(self)
        if self.player.room_id != 0:
            self.writeVint(self.roomType)
            self.writeBoolean(False)
            self.writeVint(10)

            self.writeInt(0) # Gameroom HighID
            self.writeInt(self.player.room_id) # Gameroom LowID

            self.writeVint(1557129593)
            self.writeBoolean(False)
            self.writeBoolean(False)

            self.writeVint(self.player.slot_index)
            self.writeScId(15, self.mapID)               # MapID

            # Player
            self.writeVint(self.playerCount)
            for player,values in self.playersdata.items():
                self.writeVint(self.playersdata[player]["IsHost"])       # Gameroom owner boolean
                self.writeInt(0)                                      # HighID
                self.writeInt(int(self.playersdata[player]["LowID"]))         # LowID

                self.writeScId(16, self.playersdata[player]["brawlerID"])             # BrawlerID
                self.writeVint(0)                                    #
                self.writeVint(99999)                                # Trophies
                self.writeVint(99999)                                # Trophies for rank
                self.writeVint(10)                                   # Power level

                self.writeVint(3)                                   # Player State | 11: Events, 10: Brawlers, 9: Writing..., 8: Training, 7: Spectactor, 6: Offline, 5: End Combat Screen, 4: Searching, 3: Not Ready, 2: AFK, 1: In Combat, 0: OffLine
                self.writeVint(self.playersdata[player]["Ready"])    # Is ready
                self.writeVint(self.playersdata[player]["Team"])     # Team | 0: Blue, 1: Red
                self.writeVint(0)
                self.writeVint(2)

                self.writeString(self.playersdata[player]["name"])                  # Player name
                self.writeVint(100)
                self.writeVint(28000000 + self.playersdata[player]["profileIcon"])  # Player icon
                self.writeVint(43000000 + self.playersdata[player]["namecolor"])    # Player name color

                self.writeScId(23, self.playersdata[player]["starpower"])       # Starpower

            self.writeVint(0) # Invitation array

            self.writeVint(0) # Array

            self.writeBoolean(False)
        else:
            pass
