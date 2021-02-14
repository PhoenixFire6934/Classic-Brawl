import time
from Utils.Helpers import Helpers

class EventSlots:
    Timer = 86400

    maps = [
        # Status = [3 = Nothing, 2 = Star Token, 1 = New Event]
        {
            'ID': 7,
            'Status': 3,
            'Ended': False,
            'Modifier': 0,
            'CollectReward': 10
        },

        {
            'ID': 32,
            'Status': 3,
            'Ended': False,
            'Modifier': 0,
            'CollectReward': 10
        },

        {
            'ID': 17,
            'Status': 3,
            'Ended': False,
            'Modifier': 0,
            'CollectReward': 10
        },

        {
            'ID': 0,
            'Status': 3,
            'Ended': False,
            'Modifier': 0,
            'CollectReward': 10
        },

        {
            'ID': 38,
            'Status': 3,
            'Ended': False,
            'Modifier': 0,
            'CollectReward': 10
        },

        {
            'ID': 24,
            'Status': 3,
            'Ended': False,
            'Modifier': 0,
            'CollectReward': 10
        }

    ]

    def EncodeEventSlots(self):
        count = len(EventSlots.maps)
        self.writeVint(count)

        for map in EventSlots.maps:

            self.writeVint(EventSlots.maps.index(map) + 1)
            self.writeVint(EventSlots.maps.index(map) + 1)
            self.writeVint(map['Ended'])  # IsActive | 0 = Active, 1 = Disabled
            self.writeVint(EventSlots.Timer)  # Timer

            self.writeVint(map['CollectReward'])
            self.writeScId(15, map['ID'])

            self.writeVint(map['Status'])

            self.writeString()
            self.writeVint(0)
            self.writeVint(0)  # Powerplay game played
            self.writeVint(0)  # Powerplay game left maximum

            if map['Modifier'] > 0:
                self.writeBoolean(True)  # Gamemodifier boolean
                self.writeVint(1)  # ModifierID
            else:
                self.writeBoolean(False)

            self.writeVint(0)
