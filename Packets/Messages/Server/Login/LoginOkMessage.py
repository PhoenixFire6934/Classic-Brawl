import time

from Utils.Writer import Writer


class LoginOkMessage(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.id = 20104
        self.version = 1

    def encode(self):
        self.writeInt(self.player.high_id)
        self.writeInt(1)
        # HighID, lowID
        self.writeInt(self.player.high_id)
        self.writeInt(1)
        # HighID, lowID
        self.writeString(self.player.token)  # Token
        self.writeString()
        self.writeString()

        self.writeInt(26)  # MajorVersion
        self.writeInt(165)  # Build
        self.writeInt(1)  # MinorVersion

        self.writeString("dev")  # Environment
        self.writeInt(1) 
        self.writeInt(1)  
        self.writeInt(62) 
        self.writeString()  
        self.writeString() 
        self.writeString()  
        self.writeInt(0)
        self.writeString() 
        self.writeString("RO")
        self.writeString()
        self.writeInt(1)
        self.writeString()  
        self.writeString() 
        self.writeString() 
        self.writeVint(0)
        self.writeString()
        self.writeVint(1)
