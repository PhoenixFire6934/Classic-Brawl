from Utils.Helpers import Helpers
from Database.DataBase import DataBase
from random import choice
from string import ascii_uppercase
import json

from Logic.Player import Players
from Packets.Messages.Server.Alliance.Events.AllianceEditOkMessage import AllianceEditOkMessage
from Packets.Messages.Server.Alliance.MyAllianceMessage import MyAllianceMessage

from Utils.Reader import BSMessageReader


class Edit_Settings_Message(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.clubDescription = self.read_string() # Club description

        self.inf2 = self.read_Vint() # ID Type
        self.badgeID = self.read_Vint() # Club BadgeID

        self.inf4 = self.read_Vint() # ID Type
        self.regionID = self.read_Vint() # Region ID

        self.clubType = self.read_Vint() # Club type || 1 = open, 2 = invite only, 3 = closed
        self.requiredTrophies = self.read_Vint() # Trophy required 
        self.friendlyFamilly = self.read_Vint() # Family friendly | 1 = true, 0 = false

    def process(self):
        # Replacing value   
        DataBase.replaceClubValue(self, self.player.ClubID, self.clubDescription, self.badgeID, self.clubType, self.requiredTrophies, self.friendlyFamilly)
        
        # Sending confirmation and updated data
        AllianceEditOkMessage(self.client, self.player).send()
        MyAllianceMessage(self.client, self.player, self.player.ClubID).send()