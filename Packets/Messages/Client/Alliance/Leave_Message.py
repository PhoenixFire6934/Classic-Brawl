from Packets.Messages.Server.Alliance.AllianceStreamMessage import AllianceStreamMessage
from Utils.Helpers import Helpers
from Database.DataBase import DataBase
from random import choice
from string import ascii_uppercase
import json

from Logic.Player import Players
from Packets.Messages.Server.Alliance.MyAllianceMessage import MyAllianceMessage
from Packets.Messages.Server.Alliance.Events.AllianceLeaveOkMessage import AllianceLeaveOkMessage
from Packets.Messages.Server.Alliance.AllianceChatServerMessage import AllianceChatServerMessage
from Packets.Messages.Server.Alliance.AllianceDataMessage import AllianceDataMessage

from Utils.Reader import BSMessageReader


class Leave_Message(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        pass

    def process(self):

        # Removing member 
        DataBase.loadClub(self, self.player.ClubID)

        if self.clubmembercount == 1:
            DataBase.AddMember(self, self.player.ClubID, self.player.LowID, self.player.name, 0)

        else:
            DataBase.AddMember(self, self.player.ClubID, self.player.LowID, self.player.name, 2)
            DataBase.Addmsg(self, 4, 0, self.player.LowID, self.player.name, self.player.ClubRole, 4)

        # Info
        
        AllianceLeaveOkMessage(self.client, self.player).send()
        MyAllianceMessage(self.client, self.player, self.player.ClubID).sendToOthers()
        MyAllianceMessage(self.client, self.player, 0).send()
        AllianceChatServerMessage(self.client, self.player, 4).sendToOthers()

        DataBase.replaceValue(self, 'clubID', 0)
        self.player.ClubID = 0
        DataBase.replaceValue(self, 'clubRole', 0)
        self.player.ClubRole = 0