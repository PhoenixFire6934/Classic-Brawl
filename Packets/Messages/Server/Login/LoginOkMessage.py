import time

from Utils.Writer import Writer


class LoginOkMessage(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.id = 20104
        self.version = 1

    def encode(self):
        # Account ID
        self.writeInt(self.player.high_id)
        self.writeInt(self.player.low_id)

        # Home ID
        self.writeInt(self.player.high_id)
        self.writeInt(self.player.low_id)

        self.writeString(self.player.token)  # Pass Token
        self.writeString() # Facebook ID
        self.writeString() # Gamecenter ID

        self.writeInt(24)   # Major Version
        self.writeInt(150)  # Build
        self.writeInt(0)    # Minor Version

        self.writeString("dev")  # Environment

        self.writeInt(0)  # Session Count
        self.writeInt(0)  # Play Time Seconds
        self.writeInt(0) # Days Since Started Playing

        self.writeString()  
        self.writeString() 
        self.writeString()

        self.writeInt(0)

        self.writeString()
        self.writeString("RO") # Region
        self.writeString()

        self.writeInt(1)

        self.writeString()

        self.writeInt(0) # Array

        self.writeInt(0) # Array

        self.writeVint(0)

        self.writeString()

        self.writeVint(1)
        self.writeVint(1)

        self.writeString()
