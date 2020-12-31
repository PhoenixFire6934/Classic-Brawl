from Utils.Helpers import Helpers
from Database.DataBase import DataBase
from random import choice
from string import ascii_uppercase
import json

from Utils.Reader import BSMessageReader


class Promote_Alliance_Member_Message(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.TargetHighID = self.read_int()
        self.TargetLowID = self.read_int()
        self.TargetedRole = self.read_Vint()

    def process(self):
        print("HighID", self.TargetHighID, "LowID", self.TargetLowID, "Role", self.TargetedRole)

        # Replacing value
        DataBase.replaceOtherValue(self, self.TargetLowID, 'clubRole', self.TargetedRole)
        
        # Sending confirmation and updated data