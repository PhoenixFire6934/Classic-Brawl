import time

class EventSlots:
    Timer = 86400

    maps = [
        # Status = [3 = Nothing, 2 = Star Token, 1 = New Event]
        {
            'ID': 7,
            'Status': 3,
            'Ended': False,
            'Modifier': 0,
            'Tokens': 10
        },

        {
            'ID': 32,
            'Status': 3,
            'Ended': False,
            'Modifier': 0,
            'Tokens': 10
        },

        {
            'ID': 17,
            'Status': 3,
            'Ended': False,
            'Modifier': 0,
            'Tokens': 10
        },

        {
            'ID': 0,
            'Status': 3,
            'Ended': False,
            'Modifier': 0,
            'Tokens': 10
        },

        {
            'ID': 38,
            'Status': 3,
            'Ended': False,
            'Modifier': 0,
            'Tokens': 10
        },

        {
            'ID': 24,
            'Status': 3,
            'Ended': False,
            'Modifier': 0,
            'Tokens': 10
        }


    ]

    def encodeEventSlot(self):
        # Logic Events
        count = len(EventSlots.maps)
        self.writeVint(count)
        for map in EventSlots.maps:

            self.writeVint(EventSlots.maps.index(map) + 1)
            self.writeVint(EventSlots.maps.index(map) + 1)
            self.writeBoolean(map['Ended'])  # IsActive | 0 = Active, 1 = Disabled
            self.writeVint(EventSlots.Timer)  # Timer

            self.writeVint(map["Tokens"])
            self.writeScId(15, map['ID'])

            self.writeVint(map['Status'])

            self.writeString()
            self.writeVint(0)

            if map['Modifier'] > 0:
                self.writeBoolean(True)  # Gamemodifier boolean
                self.writeVint(1)  # ModifierID
            else:
                self.writeBoolean(False)

            self.writeVint(0)