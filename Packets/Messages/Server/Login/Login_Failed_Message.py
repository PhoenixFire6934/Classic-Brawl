from Utils.Writer import Writer
from Utils.Fingerprint import Fingerprint


class LoginFailedMessage(Writer):

    def __init__(self, client, player, msg):
        super().__init__(client)
        self.id = 20103
        self.player = player
        self.msg = msg
        self.fingerprint = Fingerprint.loadFinger_full("GameAssets/fingerprint.json")

        """
        << Error Code List >>
        # 1  = Custom Message
        # 7  = Patch
        # 8  = Update Available
        # 9  = Failed to Connect
        # 10 = Maintenance
        # 11 = Banned
        # 13 = Acc Locked PopUp
        # 16 = Updating Cr/Maintenance
        # 18 = Chinese Text?
        
        """

    def encode(self):
        self.writeInt(self.player.err_code) # Error Code
        self.writeString(self.fingerprint)  # Fingerprint JSON

        self.writeString() # Server Host

        self.writeString(self.player.patch_url)  # Patch URL
        self.writeString(self.player.update_url) # Update URL
        self.writeString(self.msg)               # Message

        self.writeInt(3600)     # Estimated Time
        self.writeBoolean(False)

        self.writeString()
        self.writeString()

        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)

        self.writeString()

        self.writeInt(0)
        self.writeBoolean(False)
