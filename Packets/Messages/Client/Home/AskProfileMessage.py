from Packets.Messages.Server.Home.PlayerProfileMessage import PlayerProfileMessage
from Database.DatabaseManager import DataBase

from Utils.Reader import BSMessageReader


class AskProfileMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client


    def decode(self):
        self.high_id = self.read_int()
        self.low_id = self.read_int()


    def process(self):
        self.players = DataBase.getAllPlayers(self)
        for player in self.players:
            if self.low_id == player["lowID"]:
                self.UnlockedBrawlersList = []
                for brawler_id in player["UnlockedBrawlers"]:
                    if player["UnlockedBrawlers"][str(brawler_id)] == 1:
                        self.UnlockedBrawlersList.append(int(brawler_id))
                self.UnlockedBrawlersList = player["UnlockedBrawlers"]

                for brawler_id in self.UnlockedBrawlersList:
                        
                    def by_trophy(plr):
                            return plr['brawlersTrophies'][str(brawler_id)]

                    players = DataBase.getAllPlayers(self)
                    players.sort(key = by_trophy, reverse=True)
        if self.high_id == 0:
            PlayerProfileMessage(self.client, self.player, self.high_id, self.low_id, self.players).send()
