from Packets.Messages.Server.OutOfSyncMessage import OutOfSyncMessage
from Packets.Messages.Server.Battle.BattleTestMessage import BattleTestMessage

from Utils.Reader import BSMessageReader


class StartBattleMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client


    def decode(self):
        self.read_Vint()
        self.CardID = self.read_Vint()

        self.read_Vint()
        self.MapIndex = self.read_Vint()

        print(self.CardID, self.MapIndex)

    def process(self):
        if self.MapIndex in [1, 3, 4]:
            self.player.mmplayers = 6
        if self.MapIndex in [2, 5]:
            self.player.mmplayers = 10
        if self.MapIndex == 6:
            self.player.mmplayers = 6
        BattleTestMessage(self.client, self.player, 0).send()
