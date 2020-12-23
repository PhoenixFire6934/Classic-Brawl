import json
from Utils.Writer import Writer
from Database.DataBase import DataBase


class JoinableAllianceListMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24304
        self.player = player

    def encode(self):
        DataBase.CountClub(self, 1, 100, 2, 50)

        self.writeVint(self.AllianceCount)
        
        with open('club.db', 'r') as read_data:
            for club in read_data.readlines():

                clubData = json.loads(club)
                dict = json.loads(json.dumps(clubData))

                for ClubID, info in dict.items():
                    if info['members']['totalmembers'] >= 1 and info['members']['totalmembers'] < 100 and info['type'] <= 2:
                        
                        self.writeInt(0)                                # ClubHighID
                        self.writeInt(int(ClubID))                      # ClubLowID
                        self.writeString(info['name'])                  # Club name

                        self.writeVint(8)                               # BadgeID type 
                        self.writeVint(info['badgeID'])                 # Club badge number

                        self.writeVint(info['type'])                    # Club type

                        self.writeVint(info['members']['totalmembers']) # Member count

                        self.writeVint(info['trophies'])                # Trophies total
                        self.writeVint(info['trophiesneeded'])          # Trophies needed
                        self.writeVint(0)                               # Unknown
                        
                        self.writeString(info['region'])                # Region
                        self.writeVint(info['members']['totalmembers']) # Members online
                        self.writeVint(info['friendlyfamily'])          # Family friendly