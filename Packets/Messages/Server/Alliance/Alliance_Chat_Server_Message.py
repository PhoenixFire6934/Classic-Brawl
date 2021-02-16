from Utils.Writer import Writer
import json
from tinydb import TinyDB, Query
from Database.DatabaseManager import DataBase

class AllianceChatServerMessage(Writer):

    def __init__(self, client, player, msg_content):
        super().__init__(client)
        self.msg_content = msg_content
        self.id = 24312
        self.player = player

    def encode(self):
        DataBase.GetmsgCount(self, self.player.club_low_id)
        db = TinyDB('Database/Club/chat.db')
        query = Query()
        data = db.search(query.clubID == self.player.club_low_id)
        data = data[0]
        self.writeVint(data['info'][str(self.MessageCount)]['Event'])
        self.writeVint(0)
        self.writeVint(self.MessageCount + 1)
        self.writeVint(0)
        self.writeVint(data['info'][str(self.MessageCount)]['PlayerID'])
        self.writeString(data['info'][str(self.MessageCount)]['PlayerName'])
        self.writeVint(data['info'][str(self.MessageCount)]['PlayerRole'])
        self.writeVint(0)
        self.writeVint(0)
        if data['info'][str(self.MessageCount)]['Event'] == 4:
            self.writeVint(data['info'][str(self.MessageCount)]['Message']) # 1 = Kicked, 2 = Join request accepted, 3 = Join the club, 4 = Leave the club
            self.writeVint(1)
            self.writeVint(0)
            self.writeVint(data['info'][str(self.MessageCount)]['PlayerID'])
            self.writeString(data['info'][str(self.MessageCount)]['PlayerName'])
        else:
            self.writeString(data['info'][str(self.MessageCount)]['Message'])