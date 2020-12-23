from Utils.Reader import BSMessageReader
from Packets.Commands.Client.Select_Thumbnail import SelectThumbnail
from Packets.Commands.Client.Select_Name_Color import SelectNameColor
from Packets.Commands.Client.Buy_Brawl_Box import BuyBrawlBox
from Packets.Commands.Client.Select_Brawler import SelectBrawler
from Packets.Commands.Client.Select_Starpower import SelectStarpower
from Packets.Commands.Client.Buy_Gold import BuyGold
from Packets.Commands.Client.Buy_Token_Doubler import BuyTokenDoubler



class EndClientTurn(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.client = client
        self.player = player

    def decode(self):
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.commandID = self.read_Vint()


    def process(self):
        if self.commandID == 500 or self.commandID == 517 or self.commandID == 535 or self.commandID == 519:
            BuyBrawlBox.decode(self)
            BuyBrawlBox.process(self)

        elif self.commandID == 505:
            SelectThumbnail.decode(self)
            SelectThumbnail.process(self)

        elif self.commandID == 506:
            SelectBrawler.decode(self)
            SelectBrawler.process(self)

        elif self.commandID == 521:
            BuyGold.decode(self)
            BuyGold.process(self)

        elif self.commandID == 509:
            BuyTokenDoubler.decode(self)
            BuyTokenDoubler.process(self)

        elif self.commandID == 527:
            SelectNameColor.decode(self)
            SelectNameColor.process(self)

        elif self.commandID == 529:
            SelectStarpower.decode(self)
            SelectStarpower.process(self)

        elif self.commandID >= 0:
            print("Command ID", self.commandID, "is not handled!")
