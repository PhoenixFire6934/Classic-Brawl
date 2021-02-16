from Packets.Messages.Server.Alliance.Alliance_Data_Message import AllianceDataMessage

from Utils.Reader import BSMessageReader


class SendClubMail(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        value = []
        for i in range(30):
            value.append(self.read_Vint())
        print(value)

    def process(self):
        pass
        #AllianceDataMessage(self.client, self.player, self.clubHighID, self.clubLowID).send()