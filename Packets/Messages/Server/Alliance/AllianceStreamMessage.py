from Database.DataBase import DataBase
import json
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

            with open('chat.db', 'r') as read_data:
                for line in read_data.readlines():
                    
                    json_data = json.loads(line)
                    dict = json.loads(json.dumps(json_data))

                    if str(self.clubLowID) in dict:
                        for i in range(1, self.MessageCount + 1):
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
                                self.writeVint(dict[str(self.clubLowID)][str(i)]['Message'])
                                self.writeVint(1)
                                self.writeVint(0)
                                self.writeVint(dict[str(self.clubLowID)][str(i)]['PlayerID'])
                                self.writeString(dict[str(self.clubLowID)][str(i)]['PlayerName'])
                            else:
                                self.writeString(dict[str(self.clubLowID)][str(i)]['Message'])

        else:
            self.writeVint(0)