from Logic.Home.LogicDailyData import LogicDailyData
from Logic.Home.LogicConfData import LogicConfData

class LogicClientHome:

    def encode(self):
        LogicDailyData.encode(self)
        LogicConfData.encode(self)

        self.writeLong(self.player.ID)

        self.writeVInt(0)  # Unknown Array
        for x in range(0):
            pass

        self.writeVInt(0)  # Unknown

        self.writeUInt8(0) # Unknown
