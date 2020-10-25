from random import choice
from string import ascii_uppercase
import json

from Logic.Player import Players
from Packets.Commands.Server.Change_Name_Callback import SetNameResponse

from Utils.Reader import BSMessageReader


class SetName(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.player.name = self.read_string()

    def process(self):
        SetNameResponse(self.client, self.player).send()