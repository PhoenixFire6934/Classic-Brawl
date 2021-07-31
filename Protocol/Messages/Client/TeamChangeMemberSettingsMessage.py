from ByteStream.Reader import Reader
from Files.CsvLogic.Cards import Cards
from Files.CsvLogic.Characters import Characters
from Protocol.Messages.Server.TeamMessage import TeamMessage


class TeamChangeMemberSettingsMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client


    def decode(self):
        self.data_ref = self.readDataReference()
        if self.data_ref[0] == 0:
            self.data_ref = self.readDataReference()


    def process(self, db):
        if self.data_ref[0] == 29:
            self.player.home_brawler = Characters.get_brawler_by_skin_id(self, self.data_ref[1])
            self.player.home_skin    = self.data_ref[1]
            self.player.starpower    = Cards.get_spg_by_brawler_id(self, self.player.home_brawler, 4)
            self.player.gadget       = Cards.get_spg_by_brawler_id(self, self.player.home_brawler, 5)

        elif self.data_ref[0] == 23:
            type = Cards.check_spg_id(self, self.data_ref[1])
            if  type == '4':
                self.player.starpower = self.data_ref[1]
            elif type == '5':
                self.player.gadget = self.data_ref[1]

            db.update_player_account(self.player.token, 'StarPower', self.player.starpower)
            db.update_player_account(self.player.token, 'Gadget', self.player.gadget)


        TeamMessage(self.client, self.player).send()