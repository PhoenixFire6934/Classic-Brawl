from Utils.Writer import Writer
import json


class AllianceLeaveOkMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24333
        self.player = player

    def encode(self):
        self.writeVint(80) # Event type