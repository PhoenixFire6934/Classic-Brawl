from random import choice
from string import ascii_uppercase
import json

from Logic.Player import Players
from Packets.Messages.Server.Gameroom.TeamGameroomDataMessage import TeamGameroomDataMessage
from Packets.Messages.Server.Gameroom.TeamGameStartingMessage import TeamGameStartingMessage

from Utils.Reader import BSMessageReader


class TeamSetMemberReadyMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        pass

    def process(self):
        if(self.player.isReady == 0):
            self.player.isReady = 0
        else:
            self.player.isReady = 0
        TeamGameroomDataMessage(self.client, self.player).send()
        TeamGameStartingMessage(self.client, self.player).send()
        
