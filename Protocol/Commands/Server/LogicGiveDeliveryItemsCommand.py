from ByteStream.Writer import Writer
from Logic.Home.LogicBoxData import LogicBoxData

class LogicGiveDeliveryItemsCommand(Writer):

    def encode(self):
        if self.player.delivery_items["DeliveryTypes"] != [100]: # Check if there's other delivery types to reverse the order
            self.player.delivery_items['DeliveryTypes'] = list(reversed(self.player.delivery_items['DeliveryTypes']))

        self.writeVInt(0)
        self.writeVInt(len(self.player.delivery_items['DeliveryTypes'])) # Amount

        for y in self.player.delivery_items['DeliveryTypes']:
            # DeliveryUnit
            self.writeVInt(y)
            if y != 100:
                rewards = LogicBoxData(self.player).randomize(y)['Rewards']
            else:
                rewards = self.player.delivery_items['Items']

            self.writeVInt(len(rewards))

            for x in rewards:
                # GatchaDrop::encode
                self.writeVInt(x['Amount'])
                self.writeDataReference(*x.get("DataRef", [0, 0]))
                self.writeVInt(x['Value'])
                self.writeDataReference(*x.get("ItemID", [0, 0]))
                self.writeDataReference(*x.get("SPGID", [0, 0]))
                self.writeVInt(0)

        self.writeBoolean(True) # ForcedDrops

        self.writeVInt(1)
        self.writeVInt(1)
        self.writeVInt(0)
        self.writeVInt(0)
        # LogicServerCommand::encode
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeLogicLong(0)

    def getCommandType(self) -> int:
        return 203
