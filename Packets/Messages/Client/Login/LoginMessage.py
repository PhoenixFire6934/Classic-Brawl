from Packets.Messages.Server.Alliance.AllianceStreamMessage import AllianceStreamMessage
from Packets.Messages.Server.Login.LoginOkMessage import LoginOkMessage
from Packets.Messages.Server.Home.OwnHomeDataMessage import OwnHomeDataMessage
from Packets.Messages.Server.Alliance.MyAllianceMessage import MyAllianceMessage
from Packets.Messages.Server.Gameroom.DoNotDistrubOkMessage import DoNotDistrubOkMessage
from Packets.Messages.Server.Gameroom.TeamGameroomDataMessage import TeamGameroomDataMessage

from Packets.Messages.Server.Login.LoginFailedMessage import LoginFailedMessage
from Utils.Reader import BSMessageReader
from Utils.Helpers import Helpers
from Database.DataBase import DataBase

class LoginMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.player.HighID = self.read_int()
        self.player.LowID = self.read_int()
        self.player.Token = self.read_string()
        
        self.major = self.read_int()
        self.minor = self.read_int()
        self.build = self.read_int()

        self.fingerprint_sha = self.read_string()

    def process(self):
        if self.major != 26:
            LoginFailedMessage(self.client, self.player, "The server does not support your version").send()

        elif self.player.LowID != 0:

            if self.player.maintenance:
                LoginFailedMessage(self.client, self.player, "").send()

            if self.player.patch:
                if self.fingerprint_sha != self.player.patch_sha:
                    LoginFailedMessage(self.client, self.player, "").send()

            LoginOkMessage(self.client, self.player).send()
            DataBase.loadAccount(self) # load account
            OwnHomeDataMessage(self.client, self.player).send()

            if self.player.ClubID > 0:
                MyAllianceMessage(self.client, self.player, self.player.ClubID).send()
                AllianceStreamMessage(self.client, self.player, self.player.ClubID, 0).send()
                DataBase.GetmsgCount(self, self.player.ClubID)
                self.player.ClubMessageCount = self.MessageCount
            else:
                MyAllianceMessage(self.client, self.player, 0).send()

            if self.player.DoNotDistrub == 1:
                DoNotDistrubOkMessage(self.client, self.player).send()
            if self.player.roomID > 0:
                TeamGameroomDataMessage(self.client, self.player).send()
            
        else:
            self.player.LowID = Helpers.randomID(self)
            self.player.HighID = 0
            self.player.Token = Helpers.randomStringDigits(self)
            LoginOkMessage(self.client, self.player).send()
            OwnHomeDataMessage(self.client, self.player).send()
            if self.player.ClubID > 0:
                MyAllianceMessage(self.client, self.player, self.player.ClubID, 1).send()