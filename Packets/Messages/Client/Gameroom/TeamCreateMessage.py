from Packets.Messages.Server.Gameroom.TeamGameroomDataMessage import TeamGameroomDataMessage

from Utils.Reader import BSMessageReader

from Logic.EventSlots import EventSlots


class TeamCreateMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.read_Vint()
        self.mapID = self.read_Vint()


    def process(self):
        self.player.map_id = EventSlots.maps[self.mapID - 1]['ID']
        TeamGameroomDataMessage(self.client, self.player).send()
