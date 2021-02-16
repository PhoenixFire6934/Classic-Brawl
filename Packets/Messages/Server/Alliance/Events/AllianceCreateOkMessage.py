from Utils.Writer import Writer
import json


class AllianceCreateOkMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24333
        self.player = player

    def encode(self):
        self.writeVint(20) # Event type