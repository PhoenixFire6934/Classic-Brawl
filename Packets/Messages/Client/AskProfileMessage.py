from random import choice
from string import ascii_uppercase
import json

from Logic.Player import Players
from Packets.Messages.Server.PlayerProfileMessage import PlayerProfile

from Utils.Reader import BSMessageReader


class AskProfile(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        pass

    def process(self):
        PlayerProfile(self.client, self.player).send()