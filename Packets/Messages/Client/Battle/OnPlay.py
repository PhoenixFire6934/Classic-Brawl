from Utils.Reader import BSMessageReader
from Packets.Messages.Server.Gameroom.TeamGameroomDataMessage import TeamGameroomDataMessage
from Packets.Messages.Server.OutOfSyncMessage import OutOfSyncMessage
from Database.DatabaseManager import DataBase
from Logic.EventSlots import EventSlots
import random


class OnPlay(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client


    def decode(self):
        self.read_Vint()
        self.CardID = self.read_Vint()

        self.read_Vint()
        self.MapIndex = self.read_Vint()

        print(self.CardID, self.MapIndex)

    def process(self):
        if self.player.shouldRedirect:
            self.roomType = 1
            self.player.room_id = random.randint(0, 2147483647)
            DataBase.replaceValue(self, 'roomID', self.player.room_id)
            self.player.map_id = EventSlots.maps[self.MapIndex- 1]['ID']
            DataBase.createGameroomDB(self)
            TeamGameroomDataMessage(self.client, self.player).send()
