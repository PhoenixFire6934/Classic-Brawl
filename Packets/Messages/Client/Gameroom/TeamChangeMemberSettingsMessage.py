from Packets.Messages.Server.Gameroom.TeamGameroomDataMessage import TeamGameroomDataMessage
from Database.DatabaseManager import DataBase
from Files.CsvLogic.Characters import Characters
from Files.CsvLogic.Cards import Cards

from Utils.Reader import BSMessageReader


class TeamChangeMemberSettingsMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.read_Vint()
        self.read_Vint()
        self.player.skin_id = self.read_Vint()
        
        if self.player.skin_id in [0, 29, 52]:
            self.player.brawler_id = 0
        elif self.player.skin_id in [1, 2, 69]:
            self.player.brawler_id = 1
        elif self.player.skin_id in [3, 25, 64]:
            self.player.brawler_id = 2
        elif self.player.skin_id in [4, 5, 58, 72]:
            self.player.brawler_id = 3
        elif self.player.skin_id in [9, 26, 68]:
            self.player.brawler_id = 4
        elif self.player.skin_id in [10, 11]:
            self.player.brawler_id = 5
        elif self.player.skin_id in [12, 27, 59]:
            self.player.brawler_id = 6
        elif self.player.skin_id in [13, 44, 47]:
            self.player.brawler_id = 7
        elif self.player.skin_id in [14, 15, 60]:
            self.player.brawler_id = 8
        elif self.player.skin_id in [6, 56, 57]:
            self.player.brawler_id = 9
        elif self.player.skin_id in [7, 28, 30]:
            self.player.brawler_id = 10
        elif self.player.skin_id in [18, 50, 63]:
            self.player.brawler_id = 11
        elif self.player.skin_id in [19, 20, 49]:
            self.player.brawler_id = 12
        elif self.player.skin_id in [21, 71]:
            self.player.brawler_id = 13
        elif self.player.skin_id in [22]:
            self.player.brawler_id = 14
        elif self.player.skin_id in [23]:
            self.player.brawler_id = 15
        elif self.player.skin_id in [24]:
            self.player.brawler_id = 16
        elif self.player.skin_id in [32]:
            self.player.brawler_id = 17
        elif self.player.skin_id in [34, 70]:
            self.player.brawler_id = 18
        elif self.player.skin_id in [41, 61]:
            self.player.brawler_id = 19
        elif self.player.skin_id in [42, 45]:
            self.player.brawler_id = 20
        elif self.player.skin_id in [67]:
            self.player.brawler_id = 21
        elif self.player.skin_id in [62]:
            self.player.brawler_id = 23


    def process(self):
       

        DataBase.UpdateGameroomPlayerInfo(self, self.player.low_id)

        TeamGameroomDataMessage(self.client, self.player).send()