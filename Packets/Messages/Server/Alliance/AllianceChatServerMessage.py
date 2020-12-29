from Database.DataBase import DataBase
from Utils.Writer import Writer
import json

class AllianceChatServerMessage(Writer):

    def __init__(self, client, player, msg_content):
        super().__init__(client)
        self.msg_content = msg_content
        self.id = 24312
        self.player = player

    def encode(self):
        DataBase.GetmsgCount(self, self.player.ClubID)
        self.clubLowID = self.player.ClubID
        
        with open('chat.db', 'r') as read_data:
            for line in read_data.readlines():
                
                json_data = json.loads(line)
                dict = json.loads(json.dumps(json_data))

                if str(self.clubLowID) in dict:
                    for i in range(dict[str(self.clubLowID)]['Total'] , dict[str(self.clubLowID)]['Total'] + 1):
                        self.writeVint(dict[str(self.clubLowID)][str(i)]['Event'])
                        self.writeVint(0)
                        self.writeVint(dict[str(self.clubLowID)][str(i)]['Tick'])
                        self.writeVint(0)
                        self.writeVint(dict[str(self.clubLowID)][str(i)]['PlayerID'])
                        self.writeString(dict[str(self.clubLowID)][str(i)]['PlayerName'])
                        self.writeVint(dict[str(self.clubLowID)][str(i)]['PlayerRole'])
                        self.writeVint(0)
                        self.writeVint(0)
                        if dict[str(self.clubLowID)][str(i)]['Event'] == 4:
                            self.writeVint(dict[str(self.clubLowID)][str(i)]['Message']) # 1 = Kicked, 2 = Join request accepted, 3 = Join the club, 4 = Leave the club
                            self.writeVint(1)
                            self.writeVint(0)
                            self.writeVint(dict[str(self.clubLowID)][str(i)]['PlayerID'])
                            self.writeString(dict[str(self.clubLowID)][str(i)]['PlayerName'])
                        elif dict[str(self.clubLowID)][str(i)]['Event'] == 2:
                            self.writeString(dict[str(self.clubLowID)][str(i)]['Message'])
                        break