from ByteStream.Reader import Reader
from Protocol.Messages.Server.TeamMessage import TeamMessage
from Logic.Home.LogicEventData import LogicEventData

class TeamCreateMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.map_slot  = self.readVInt()
        self.map_id    = self.readVInt()
        self.room_type = self.readVInt()

    def process(self, db):
        if self.map_slot != -64:
            self.player.map_id = LogicEventData.events[self.map_slot - 1]['ID']
        else:
            self.player.map_id = 7

        TeamMessage(self.client, self.player).send()