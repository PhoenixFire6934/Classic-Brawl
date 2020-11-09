from random import choice
from string import ascii_uppercase
import json

from Logic.Player import Players
from Packets.Messages.Server.DoNotDistrubOkMessage import DoNotDistrubOkMessage
from Database.DataBase import DataBase

from Utils.Reader import BSMessageReader


class DoNotDistrubMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.player.DoNotDistrubMessage = self.read_Vint()

    def process(self):
        DataBase.replaceValue(self, 'DoNotDistrub', self.player.DoNotDistrubMessage)
        DoNotDistrubOkMessage(self.client, self.player).send()