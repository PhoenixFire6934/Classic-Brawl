from Utils.Writer import Writer
from Database.DataBase import DataBase
import json


class AllianceSearchResultMessage(Writer):

    def __init__(self, client, player, requestedName, allianceCount):
        super().__init__(client)
        self.id = 24310
        self.player = player
        self.requestedName = str(requestedName)
        self.allianceCount = allianceCount

    def encode(self):
        self.writeString(self.requestedName)
        self.writeVint(self.allianceCount)
        with open('club.db', 'r') as read_data:
            for club in read_data.readlines():

                clubData = json.loads(club)
                dict = json.loads(json.dumps(clubData))

                for name, info in dict.items():
                    if info['membercount'] > 0 and info['membercount'] < 100 and info['type'] <= 2:
                        if self.requestedName.lower() in info['name'].lower():

                            self.writeVint(0)
                            self.writeVint(0)
                            self.writeVint(0)
                            self.writeVint(0)
                            self.writeInt(int(name)) 
                            self.writeString(info['name'])
                            self.writeVint(8)
                            self.writeVint(info['badgeID']) 
                            self.writeVint(info['type']) 
                            self.writeVint(info['membercount'])
                            self.writeVint(info['trophies'])
                            self.writeVint(info['trophiesneeded'])
                            self.writeVint(0)
                            self.writeString(info['region'])
                            self.writeVint(info['membercount']) # Members online
                            self.writeVint(info['friendlyfamily']) # Family friendly