from Packets.Messages.Server.Gameroom.TeamGameroomDataMessage import TeamGameroomDataMessage
from Logic.EventSlots import EventSlots
from Database.DatabaseManager import DataBase
import random

from Utils.Reader import BSMessageReader


class TeamCreateMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.mapSlot = self.read_Vint()
        self.player.map_id = self.read_Vint()
        self.roomType = self.read_Vint()

        if self.player.map_id == -64:
            self.mapSlot = 0
            self.player.map_id = 7
        else:
            self.player.map_id = EventSlots.maps[self.mapSlot - 1]['ID']

    def process(self):
        self.player.room_id = random.randint(0, 2147483647)
        DataBase.replaceValue(self, 'roomID', self.player.room_id)

        DataBase.createGameroomDB(self)
        TeamGameroomDataMessage(self.client, self.player).send()
