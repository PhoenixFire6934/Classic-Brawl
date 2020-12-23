from Packets.Messages.Server.Gameroom.Team_Gameroom_Data_Message import TeamGameroomDataMessage

from Utils.Reader import BSMessageReader


class TeamUseGadgetMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.player.use_gadget = self.read_Vint()

    def process(self):
        TeamGameroomDataMessage(self.client, self.player).send()