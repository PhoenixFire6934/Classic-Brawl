from ByteStream.Writer import Writer
from Logic.Home.LogicBoxData import LogicBoxData

class LogicGiveDeliveryItemsCommand(Writer):

    def encode(self):
        if self.player.delivery_items["DeliveryTypes"] != [100]:
            self.player.delivery_items['DeliveryTypes'] = list(reversed(self.player.delivery_items['DeliveryTypes']))

        self.writeVInt(0)
        self.writeVInt(len(self.player.delivery_items['DeliveryTypes']))

        for y in self.player.delivery_items['DeliveryTypes']:
            self.writeVInt(y)
            if y != 100:
                box_data = LogicBoxData()
                box_data.player = self.player
                box_data.player.db = self.player.db 
                rewards = box_data.randomize(y)['Rewards']
            else:
                rewards = self.player.delivery_items['Items']

            self.writeVInt(len(rewards))

            for x in rewards:
                self.writeVInt(x['Amount'])
                self.writeDataReference(*x.get("DataRef", [0, 0]))
                self.writeVInt(x['Value'])
                self.writeDataReference(*x.get("ItemID", [0, 0]))
                self.writeDataReference(*x.get("SPGID", [0, 0]))
                self.writeVInt(0)

        self.writeBoolean(True)
        self.writeVInt(1)
        self.writeVInt(1)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeLogicLong(0)

    def getCommandType(self) -> int:
        return 203
