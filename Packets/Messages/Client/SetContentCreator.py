from random import choice
from string import ascii_uppercase
import json

from Logic.Player import Players
from database.DataBase import DataBase
from Packets.Messages.Server.OutOfSync import OutOfSync

from Utils.Reader import BSMessageReader


class SetContentCreator(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.string = self.read_string()
        if self.string.lower() == 'reset':
            DataBase.replaceValue(self, 'gold', 99999)
            DataBase.replaceValue(self, 'gems', 99999)
            DataBase.replaceValue(self, 'tickets', 99999)

    def process(self):
        OutOfSync(self.client, self.player).send()