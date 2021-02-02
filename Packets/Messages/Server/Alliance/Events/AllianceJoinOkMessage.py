from Utils.Writer import Writer
import json


class AllianceJoinOkMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24333
        self.player = player

    def encode(self):
        self.writeVint(40) # Event type