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
        if self.eventType == 1:

            with open('chat.db', 'r') as read_data:
                for line in read_data.readlines():
                    
                    json_data = json.loads(line)
                    dict = json.loads(json.dumps(json_data))

                    if str(self.clubLowID) in dict:
                        self.writeVint(dict[str(self.clubLowID)]['Total'] + 1 - self.player.OldMessageCount) # Message count
                        print(dict[str(self.clubLowID)]['Total'] + 1 - self.player.OldMessageCount, "Message to update")
                        print("OldMessageCount:", self.player.OldMessageCount, "TotalMessageCount:", dict[str(self.clubLowID)]['Total'] + 1)
                        for i in range(self.player.OldMessageCount, dict[str(self.clubLowID)]['Total'] + 1):
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
                                
        elif self.clubLowID != 0:
            DataBase.GetmsgCount(self, self.clubLowID)

            self.writeVint(self.MessageCount) # Message count

            with open('chat.db', 'r') as read_data:
                for line in read_data.readlines():
                    
                    json_data = json.loads(line)
                    dict = json.loads(json.dumps(json_data))

                    if str(self.clubLowID) in dict:
                        for i in range(dict[str(self.clubLowID)]['Total']):
                            self.writeVint(dict[str(self.clubLowID)][str(i + 1)]['Event'])
                            self.writeVint(0)
                            self.writeVint(dict[str(self.clubLowID)][str(i + 1)]['Tick'])
                            self.writeVint(0)
                            self.writeVint(dict[str(self.clubLowID)][str(i + 1)]['PlayerID'])
                            self.writeString(dict[str(self.clubLowID)][str(i + 1)]['PlayerName'])
                            self.writeVint(dict[str(self.clubLowID)][str(i + 1)]['PlayerRole'])
                            self.writeVint(0)
                            self.writeVint(0)
                            if dict[str(self.clubLowID)][str(i + 1)]['Event'] == 4:
                                self.writeVint(dict[str(self.clubLowID)][str(i + 1)]['Message']) # 1 = Kicked, 2 = Join request accepted, 3 = Join the club, 4 = Leave the club
                                self.writeVint(1)
                                self.writeVint(0)
                                self.writeVint(dict[str(self.clubLowID)][str(i + 1)]['PlayerID'])
                                self.writeString(dict[str(self.clubLowID)][str(i + 1)]['PlayerName'])
                            elif dict[str(self.clubLowID)][str(i + 1)]['Event'] == 2:
                                self.writeString(dict[str(self.clubLowID)][str(i + 1)]['Message'])

        else:
            self.writeVint(0)