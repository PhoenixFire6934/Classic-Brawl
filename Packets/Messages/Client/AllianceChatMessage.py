from random import choice
from string import ascii_uppercase
import json

from Logic.Player import Players
from Packets.Messages.Server.AllianceChatServerMessage import AllianceChatServerMessage

from Utils.Reader import BSMessageReader


class AllianceChatMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.msg = self.read_string()



    def process(self):
        AllianceChatServerMessage(self.client, self.player, self.msg).send()
        self.player.messageTick += 1