from Utils.Writer import Writer
from Database.DatabaseManager import DataBase

class FriendListUpdateMessage(Writer):

    def __init__(self, client, player, friendLowID, players):
        super().__init__(client)
        self.id = 20106
        self.player = player
        self.friendID = friendLowID
        self.players = players

    def encode(self):
        self.indexOfPlayer = 1
        
        self.writeVint(len(self.players)) # Playera Count
        for player in self.players:
            if player["lowID"] == self.player.low_id:
                self.indexOfPlayer = self.players.index(player) + 1

            self.writeInt(0)  # HighID
            self.writeInt(player["lowID"])  # LowID

            self.writeString(player['name'])
            self.writeString()
            self.writeString()
            self.writeString()


            self.writeInt(28)  # Trophies
            self.writeInt(player['trophies'])  # Friend state 0 = friend, 1 = not friend, 2 = request sent, 3 = you have an invite from him??, 4 = friend list
            self.writeInt(0)
            self.writeInt(0)
            self.writeInt(0)
            self.writeInt(0)
        
            if player["clubID"] != 0:
                DataBase.loadClub(self, player["clubID"])

                self.writeBoolean(True)  # Is in club
           
                self.writeInt(0)
                self.writeInt(0)
                self.writeInt(0)
                self.writeString(self.clubName)
                self.writeInt(0)
                self.writeInt(0)    
            else:
                self.writeBoolean(False)  # Is in club
            
            self.writeString()
        
            self.writeInt(28000000 + player["profileIcon"])
            self.writeInt(0)