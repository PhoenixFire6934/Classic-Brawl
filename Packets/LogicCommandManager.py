from Utils.Reader import BSMessageReader
from Packets.Commands.Client.LogicUpgradeBrawler import Upgrade_Brawler
from Packets.Commands.Client.LogicSetPlayerThumbnailCommand import LogicSetPlayerThumbnailCommand
from Packets.Commands.Client.LogicSetPlayerNameColorCommand import LogicSetPlayerNameColorCommand
from Packets.Commands.Client.LogicPurchaseBoxCommand import LogicPurchaseBoxCommand
from Packets.Commands.Client.LogicPurchaseBoxCommand2 import LogicPurchaseBoxCommand2
from Packets.Commands.Client.LogicPurchaseOfferCommand import LogicPurchaseOfferCommand
from Packets.Commands.Client.LogicSelectSkinCommand import LogicSelectSkinCommand
from Packets.Commands.Client.LogicSetPlayerStarpowerCommand import LogicSetPlayerStarpowerCommand
from Packets.Commands.Client.LogicPurchaseHeroLvlUpMaterialCommand import LogicPurchaseHeroLvlUpMaterialCommand
from Packets.Commands.Client.LogicPurchaseDoubleCoinsCommand import LogicPurchaseDoubleCoinsCommand
from Packets.Commands.Client.LogicRemoveNewTagBrawler import LogicRemoveNewTagBrawler
from Database.DatabaseManager import DataBase


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
        if self.commandID == 500 or self.commandID == 517 or self.commandID == 535:
            LogicPurchaseBoxCommand.decode(self)
            LogicPurchaseBoxCommand.process(self)

        elif self.commandID == 519:
            LogicPurchaseOfferCommand.decode(self)
            LogicPurchaseOfferCommand.process(self)
            
        elif self.commandID == 203:
            LogicPurchaseBoxCommand2.decode(self)
            LogicPurchaseBoxCommand2.process(self)
            
        elif self.commandID == 505:
            LogicSetPlayerThumbnailCommand.decode(self)
            LogicSetPlayerThumbnailCommand.process(self)

        elif self.commandID == 506:
            LogicSelectSkinCommand.decode(self)
            LogicSelectSkinCommand.process(self)

        elif self.commandID == 520:
            Upgrade_Brawler.decode(self)
            Upgrade_Brawler.process(self)

        elif self.commandID == 521:
            LogicPurchaseHeroLvlUpMaterialCommand.decode(self)
            LogicPurchaseHeroLvlUpMaterialCommand.process(self)

        elif self.commandID == 522:
            LogicRemoveNewTagBrawler.decode(self)
            LogicRemoveNewTagBrawler.process(self)

        elif self.commandID == 509:
            LogicPurchaseDoubleCoinsCommand.decode(self)
            LogicPurchaseDoubleCoinsCommand.process(self)

        elif self.commandID == 527:
            LogicSetPlayerNameColorCommand.decode(self)
            LogicSetPlayerNameColorCommand.process(self)

        elif self.commandID == 529:
            LogicSetPlayerStarpowerCommand.decode(self)
            LogicSetPlayerStarpowerCommand.process(self)

        elif self.commandID >= 0:
            print(self.commandID, "Is not handled!")
