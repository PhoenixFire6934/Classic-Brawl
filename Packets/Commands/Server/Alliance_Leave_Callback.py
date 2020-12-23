from os import write
from Utils.Writer import Writer
import json


class AllianceLeaveCallback(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24111
        self.player = player

    def encode(self):
        pass