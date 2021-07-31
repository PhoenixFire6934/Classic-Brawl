from ByteStream.Writer import Writer
from Logic.Home.LogicBoxData import LogicBoxData

class LogicGiveDeliveryItemsCommand(Writer):

    def encode(self):

        self.writeVInt(0)
        self.writeVInt(self.player.delivery_items['Count']) # multiplier

        for y in range(self.player.delivery_items['Count']):
            # DeliveryUnit
            type = self.player.delivery_items['Type']
            self.writeVInt(type)
            if type != 100:
                rewards = LogicBoxData.randomize(self, type)['Rewards']
            else:
                rewards = self.player.delivery_items['Items']

            self.writeVInt(len(rewards))

            for x in rewards:
                # GatchaDrop
                self.writeVInt(x['Amount'])
                self.writeDataReference(x['DataRef'][0], x['DataRef'][1])
                self.writeVInt(x['Value'])
                self.writeDataReference(0, 0)
                self.writeDataReference(0, 0)
                self.writeVInt(0)

        self.writeBool(True) # ForcedDrops

        self.writeVInt(1)
        self.writeVInt(1)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeLogicLong(0)





