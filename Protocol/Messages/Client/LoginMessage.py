from ByteStream.Reader import Reader
from Utils.Helpers import Helpers
from Protocol.Messages.Server.LoginOkMessage import LoginOkMessage
from Protocol.Messages.Server.LoginFailedMessage import LoginFailedMessage
from Protocol.Messages.Server.OwnHomeDataMessage import OwnHomeDataMessage
from Protocol.Messages.Server.MyAllianceMessage import MyAllianceMessage
from Protocol.Messages.Server.AllianceStreamMessage import AllianceStreamMessage


class LoginMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client
        self.helpers = Helpers()

    def decode(self):

        self.account_id    = self.readLong()
        self.account_token = self.readString()
        self.game_major    = self.readInt()
        self.game_minor    = self.readInt()
        self.game_build    = self.readInt()

        self.fingerprint_sha = self.readString()


    def process(self, db):

        if self.player.maintenance:
            self.player.err_code = 10
            LoginFailedMessage(self.client, self.player, '').send()

        if self.fingerprint_sha != self.player.patch_sha and self.player.patch:
            self.player.err_code = 7
            LoginFailedMessage(self.client, self.player, "").send()

        if self.account_id == 0:
            self.player.ID    = self.helpers.randomID()
            self.player.token = self.helpers.randomToken()
            db.create_player_account(self.player.ID, self.player.token)

        else:
            self.player.ID = self.account_id
            self.player.token = self.account_token

            player_data = db.load_player_account(self.player.ID, self.player.token)

            if player_data:
                Helpers.load_account(self, player_data)
                club_data = db.load_club(self.player.club_id)
                Helpers.load_club(self, club_data)
            else:
                self.player.err_code = 1
                LoginFailedMessage(self.client, self.player, "Account not found in database!\nPlease clear app data.").send()


        LoginOkMessage(self.client, self.player, self.player.ID, self.player.token).send()
        OwnHomeDataMessage(self.client, self.player).send()

        if self.player.club_id != 0:
            club_data = db.load_club(self.player.club_id)
            MyAllianceMessage(self.client, self.player, club_data).send()
            AllianceStreamMessage(self.client, self.player, club_data['Messages']).send()


