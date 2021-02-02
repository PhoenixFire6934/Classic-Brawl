from Packets.Messages.Server.Gameroom.TeamGameroomDataMessage import TeamGameroomDataMessage
from Database.DatabaseManager import DataBase
import random

from Utils.Reader import BSMessageReader


class TeamCreateMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.player.map_id = 1

    def process(self):
        self.player.room_id = random.randint(0, 2147483647)
        DataBase.replaceValue(self, 'roomID', self.player.room_id)

        DataBase.createGameroomDB(self)
        TeamGameroomDataMessage(self.client, self.player).send()
