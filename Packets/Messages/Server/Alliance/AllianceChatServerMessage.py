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
        with open('chat.db', 'r') as read_data:
            for line in read_data.readlines():
                
                json_data = json.loads(line)
                dict = json.loads(json.dumps(json_data))

                if str(self.player.ClubID) in dict:
                    self.writeVint(dict[str(self.player.ClubID)][str(self.player.messageTick)]['Event'])
                    self.writeVint(0)
                    self.writeVint(dict[str(self.player.ClubID)][str(self.player.messageTick)]['Tick'])
                    self.writeVint(0)
                    self.writeVint(dict[str(self.player.ClubID)][str(self.player.messageTick)]['PlayerID'])
                    self.writeString(dict[str(self.player.ClubID)][str(self.player.messageTick)]['PlayerName'])
                    self.writeVint(dict[str(self.player.ClubID)][str(self.player.messageTick)]['PlayerRole'])
                    self.writeVint(0)
                    self.writeVint(0)
                    if dict[str(self.player.ClubID)][str(self.player.messageTick)]['Event'] == 4:
                        self.writeVint(dict[str(self.player.ClubID)][str(self.player.messageTick)]['Message']) # 1 = Kicked, 2 = Join request accepted, 3 = Join the club, 4 = Leave the club
                        self.writeVint(1)
                        self.writeVint(0)
                        self.writeVint(dict[str(self.player.ClubID)][str(self.player.messageTick)]['PlayerID'])
                        self.writeString(dict[str(self.player.ClubID)][str(self.player.messageTick)]['PlayerName'])
                    elif dict[str(self.player.ClubID)][str(self.player.messageTick)]['Event'] == 2:
                        self.writeString(dict[str(self.player.ClubID)][str(self.player.messageTick)]['Message'])