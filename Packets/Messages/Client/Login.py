from random import choice
from string import ascii_uppercase
import json
import time

from Logic.Player import Players
from Packets.Messages.Server.LoginOk import LoginOk
from Packets.Messages.Server.OwnHomeData import OwnHomeData
from Packets.Messages.Server.DoNotDistrubServer import DoNotDistrubServer
from Packets.Messages.Server.GameroomData import GameroomData

from Packets.Messages.Server.LoginFailed import LoginFailed
from Utils.Reader import BSMessageReader
from Utils.Helpers import Helpers
from database.DataBase import DataBase

class Login(BSMessageReader):
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

    def process(self):
        if self.major != 26:
            LoginFailed(self.client, self.player).send()
        elif self.player.LowID != 0:
            LoginOk(self.client, self.player).send()
            DataBase.loadAccount(self) # load account
            OwnHomeData(self.client, self.player).send()
            if self.player.DoNotDistrub == 1:
                DoNotDistrubServer(self.client, self.player).send()
            if self.player.roomID > 0:
                GameroomData(self.client, self.player).send()
            
        else:
            self.player.LowID = Helpers.randomID(self)
            self.player.HighID = 0
            self.player.Token = Helpers.randomStringDigits(self)
            LoginOk(self.client, self.player).send()
            OwnHomeData(self.client, self.player).send()
            