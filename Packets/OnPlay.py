from Packets.Messages.Server.Battle.Battle_Result_Message import BattleResultMessage
from Packets.Messages.Server.Battle.Battle_Result2_Message import BattleResult2Message
from Packets.Messages.Server.Out_Of_Sync_Message import OutOfSyncMessage

from Utils.Reader import BSMessageReader


class OnPlay(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client


    def decode(self):
        pass

    def process(self):
        OutOfSyncMessage(self.client, self.player, "Multiplayer Isn't Sync Yet").send()
        