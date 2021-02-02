from time import daylight
from random import choice
from string import ascii_uppercase
import json

from Logic.Player import Players
from Packets.Messages.Server.Alliance.My_Alliance_Message import MyAllianceMessage
from Packets.Messages.Server.Alliance.AllianceStreamMessage import AllianceStreamMessage
from Packets.Messages.Server.Alliance.Events.AllianceJoinOkMessage import AllianceJoinOkMessage
from Database.DatabaseManager import DataBase
from Utils.Helpers import Helpers

from Utils.Reader import BSMessageReader


class Create_Message(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        # ClubID
        self.clubHighID = 0
        self.clubLowID = Helpers.randomClubID(self)

        # Info
        self.clubName           = self.read_string()    # Club name 
        self.clubdescription    = self.read_string()    # Club description

        # Badge
        self.BadgeIdentifier    = self.read_Vint()      # Badge Identifier
        self.clubbadgeID        = self.read_Vint()      # BadgeID

        # Region
        self.RegionIdentifier   = self.read_Vint()      # Region Identifier
        self.clubregionID       = self.read_Vint()      # RegionID 

        # Settings
        self.clubtype           = self.read_Vint()      # Type
        self.clubtrophiesneeded = self.read_Vint()      # Trophy required
        self.clubfriendlyfamily = self.read_Vint()      # Family friendly

    def process(self):
        DataBase.replaceValue(self, 'clubID', self.clubLowID)
        self.player.club_low_id = self.clubLowID
        DataBase.replaceValue(self, 'clubRole', 2)
        self.player.club_role = 2

        # Club creation
        DataBase.createClub(self, self.clubLowID)

        # Club data
        AllianceJoinOkMessage(self.client, self.player).send()
        MyAllianceMessage(self.client, self.player, self.clubLowID).send()
        #AllianceStreamMessage(self.client, self.player, self.clubLowID, 0).send()