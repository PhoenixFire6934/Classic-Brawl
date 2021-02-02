from Packets.Messages.Server.Gameroom.TeamGameroomDataMessage import TeamGameroomDataMessage
from Database.DatabaseManager import DataBase
from Logic.EventSlots import EventSlots

from Utils.Reader import BSMessageReader

class TeamSetRankedLocationMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.player.slot_index = self.read_Vint()
        self.player.map_id = EventSlots.maps[self.player.slot_index - 1]["ID"]

    def process(self):
        DataBase.replaceGameroomValue(self, 'mapID', self.player.map_id, "room")
        TeamGameroomDataMessage(self.client, self.player).send()