from Packets.Messages.Server.Gameroom.TeamGameroomDataMessage import TeamGameroomDataMessage
from Database.DatabaseManager import DataBase
from Files.CsvLogic.Cards import Cards

from Utils.Reader import BSMessageReader


class TeamChangeMemberSettingsMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.read_Vint()
        if self.read_Vint() == 29:
            self.csv_id = 29
            self.BrawlerSkinId = self.read_Vint()

    def process(self):
        self.player.skin_id = self.BrawlerSkinId

        self.player.starpower = Cards.get_spg_by_brawler_id(self, self.player.brawler_id, 4)

        DataBase.replaceValue(self, 'starpower', self.player.starpower)

        DataBase.UpdateGameroomPlayerInfo(self, self.player.low_id)

        TeamGameroomDataMessage(self.client, self.player).send()