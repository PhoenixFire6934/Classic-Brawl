from Database.DatabaseManager import DataBase
import json
from tinydb import TinyDB, Query
from Utils.Writer import Writer


class AllianceStreamMessage(Writer):

    def __init__(self, client, player, clubLowID, type):
        super().__init__(client)
        # self.msg_content = msg_content
        self.id = 24311
        self.player = player
        self.eventType = type
        self.clubLowID = clubLowID

    def encode(self):
        if self.clubLowID != 0:
            DataBase.GetmsgCount(self, self.clubLowID)
            self.writeVint(self.MessageCount) # Message count
            db = TinyDB('Database/Club/chat.db')
            query = Query()
            data = db.search(query.clubID == self.player.club_low_id)
            data = data[0]
            for i in range(1, self.MessageCount + 1):
                self.writeVint(data['info'][str(i)]['Event'])
                self.writeVint(0)
                self.writeVint(data['info'][str(i)]['Tick'])
                self.writeVint(0)
                self.writeVint(data['info'][str(i)]['PlayerID'])
                self.writeString(data['info'][str(i)]['PlayerName'])
                self.writeVint(data['info'][str(i)]['PlayerRole'])
                self.writeVint(0)
                self.writeVint(0)
                if data['info'][str(i)]['Event'] == 4:
                    self.writeVint(data['info'][str(i)]['Message'])  # 1 = Kicked, 2 = Join request accepted, 3 = Join the club, 4 = Leave the club
                    self.writeVint(1)
                    self.writeVint(0)
                    self.writeVint(data['info'][str(i)]['PlayerID'])
                    self.writeString(data['info'][str(i)]['PlayerName'])
                else:
                    self.writeString(data['info'][str(i)]['Message'])

        else:
            self.writeVint(0)