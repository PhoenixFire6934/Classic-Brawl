from random import choice
from string import ascii_uppercase
import json

from Logic.Player import Players
from Database.DataBase import DataBase
from Packets.Messages.Server.OutOfSyncMessage import OutOfSync

from Utils.Reader import BSMessageReader


class SetContentCreator(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client
        self.send_ofs = False

    def decode(self):
        self.string = self.read_string()

        if self.string.lower() == 'reset':
            self.send_ofs = True
            DataBase.replaceValue(self, 'gold', 99999)
            DataBase.replaceValue(self, 'gems', 99999)
            DataBase.replaceValue(self, 'tickets', 99999)

        elif self.string.lower().startswith('gems'):
            newGems = self.string.split(" ", 4)[1:]
            try:
                DataBase.replaceValue(self, 'gems', int(newGems[0]))
                self.send_ofs = True
            except ValueError:
                pass

        elif self.string.lower().startswith('gold'):
            newGold = self.string.split(" ", 4)[1:]
            try:
                DataBase.replaceValue(self, 'gold', int(newGold[0]))
                self.send_ofs = True
            except ValueError:
                pass

        elif self.string.lower().startswith('tickets'):
            newTickets = self.string.split(" ", 7)[1:]
            try:
                DataBase.replaceValue(self, 'tickets', int(newTickets[0]))
                self.send_ofs = True
            except ValueError:
                pass

    def process(self):
        if self.send_ofs:
            OutOfSync(self.client, self.player, 'Changes have been applied').send()