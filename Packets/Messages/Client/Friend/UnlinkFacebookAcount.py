from Packets.Messages.Server.Friend.Events.FBAccountDisconnectedOKMessage import FBAccountDisconnectedOKMessage
from Database.DatabaseManager import DataBase

from Utils.Reader import BSMessageReader

class UnlinkFacebookAcount(BSMessageReader):

    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.read_Vint()
        self.player.FacebookID = self.read_string()
        self.player.FacebookToken = self.read_string()

    def process(self):
        if self.player.IsFacebookLinked == 1:
            self.player.IsFacebookLinked = 0
            DataBase.replaceValue(self, 'isFBLinked', 0)
            DataBase.replaceValue(self, 'facebookID', "None")
            DataBase.replaceValue(self, 'facebookToken', "None")

            FBAccountDisconnectedOKMessage(self.client, self.player).send()