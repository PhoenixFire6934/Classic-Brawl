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

        self.writeInt(20)   # Major Version
        self.writeInt(93)  # Build
        self.writeInt(1)    # Minor Version

        self.writeString("dev")  # Environment

        self.writeInt(0)  # Session Count
        self.writeInt(0)  # Play Time Seconds
        self.writeInt(0) # Days Since Started Playing

        self.writeString()  
        self.writeString() 
        self.writeString()

        self.writeInt(0)

        self.writeString()

        self.writeString("RU") # Region
        self.writeString()

        self.writeInt(1)

        self.writeString()  
        self.writeString() 
        self.writeString()

        self.writeVint(0)

        self.writeString()

        self.writeVint(1)