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
        self.player.high_id = self.read_int()
        self.player.low_id = self.read_int()
        self.player.token = self.read_string()
        self.major = self.read_int()
        self.minor = self.read_int()
        self.build = self.read_int()
        self.fingerprint_sha = self.read_string()

    def process(self):
        if self.major != 26:
            self.player.err_code = 8
            LoginFailedMessage(self.client, self.player, "Your client is outdated, click below to download the new version!").send()

        elif self.player.low_id != 0:

            if self.player.maintenance:
                LoginFailedMessage(self.client, self.player, "").send()

            if self.player.patch:
                if self.fingerprint_sha != self.player.patch_sha:
                    LoginFailedMessage(self.client, self.player, "").send()


            LoginOkMessage(self.client, self.player).send()
            DataBase.loadAccount(self) # load account
            OwnHomeDataMessage(self.client, self.player).send()
            MyAllianceMessage(self.client, self.player).send()
            if self.player.do_not_distrub == 1:
                DoNotDistrubOkMessage(self.client, self.player).send()
            if self.player.room_id > 0:
                TeamGameroomDataMessage(self.client, self.player).send()
            
        else:
            self.player.low_id = Helpers.randomID(self)
            self.player.high_id = 0
            self.player.token = Helpers.randomStringDigits(self)

            LoginOkMessage(self.client, self.player).send()
            OwnHomeDataMessage(self.client, self.player).send()
            MyAllianceMessage(self.client, self.player).send()
            