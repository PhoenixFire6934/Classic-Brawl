from datetime import datetime
from Logic.Home.LogicEventData import LogicEventData
from Logic.Home.LogicShopData import LogicShopData

class LogicConfData:

    def encode(self):

        LogicShopData.encodeShopResources(self)

        self.writeVInt(500)    # Unknown
        self.writeVInt(50)     # Unknown
        self.writeVInt(999900) # Unknown

        self.writeVInt(0)
        for x in range(0):
            self.writeVInt(x)

        LogicEventData.encode(self)

        LogicShopData.encodeShopPacks(self)

        self.writeVInt(0)   # Unknown
        self.writeVInt(200) # Max Tokens
        self.writeVInt(20)  # Plus Tokens
        self.writeVInt(0)   # Unknown
        self.writeVInt(10)  # Unknown
        self.writeVInt(0)   # Unknown
        self.writeVInt(0)   # Unknown
        self.writeVInt(0)   # Unknown
        self.writeVInt(0)   # Unknown
        self.writeUInt8(1)  # Shop Box State

        self.writeVInt(0)  # Unknown Array
        for x in range(0):
            # ReleaseEntry::encode
            self.writeDataReference(16,0)
            self.writeInt(99999)
            self.writeInt(0)

        self.writeVInt(1)  # Menu Theme Array
        for x in range(1):
            # IntValueEntry::encode
            self.writeInt(1)         # Unknown
            self.writeInt(41000000 + self.player.theme_id)  # Theme ID

        self.writeVInt(0)
        for x in range(0):
            # CustomEvent::encode
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
