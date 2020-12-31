from Packets.Commands.Server.Buy_Brawl_Box_Callback import BuyBrawlBoxCallback
from Packets.Messages.Server.Out_Of_Sync_Message import OutOfSyncMessage
from Logic.Shop import Shop

from Utils.Reader import BSMessageReader

class BuyOffer(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.offer_index = self.read_Vint()


    def process(self):
        id = Shop.offers[self.offer_index]['ID']

        if id in [0, 6, 10, 14]:

            if id in [0, 6]:
                self.player.box_id = 5

            elif id == 14:
                self.player.box_id = 4

            elif id == 10:
                self.player.box_id = 3

            BuyBrawlBoxCallback(self.client, self.player).send()

        else:
            OutOfSyncMessage(self.client, self.player, f'Claiming offer with type {id} is not supported yet').send()

