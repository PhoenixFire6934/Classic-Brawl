from Packets.Messages.Server.Gameroom.TeamGameroomDataMessage import TeamGameroomDataMessage

from Utils.Reader import BSMessageReader


class TeamCreateMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.read_Vint()
        self.mapID = self.read_Vint()



    def process(self):
        if self.mapID == 1:
            self.player.mapID = 7 # gem grab
        elif self.mapID == 2:
            self.player.mapID = 32 # solo sd
        elif self.mapID == 3:
            self.player.mapID = 17 # heist
        elif self.mapID == 4:
            self.player.mapID = 0 # bounty
        elif self.mapID == 5:
            self.player.mapID = 24 # brawl ball
        elif self.mapID == 6:
            self.player.mapID = 202 # present plunder
        elif self.mapID == 7:
            self.player.mapID = 97 # siege
        elif self.mapID == 8:
            self.player.mapID = 167 # takedown
        elif self.mapID == 9:
            self.player.mapID = 174 # lone star
        TeamGameroomDataMessage(self.client, self.player).send()
