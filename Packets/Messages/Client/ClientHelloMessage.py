from random import choice
from string import ascii_uppercase
import json

from Logic.Player import Players
from Packets.Messages.Server.LoginFailedMessage import LoginFailed

from Utils.Reader import BSMessageReader

class ClientHello(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        pass

    def process(self):
        self.player.errorID = 8 
        self.player.errorText = "The server does not support your version"
        LoginFailed(self.client, self.player).send()