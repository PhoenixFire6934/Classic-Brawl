from Packets.Messages.Server.Alliance.AllianceStreamMessage import AllianceStreamMessage
from Utils.Helpers import Helpers
from Database.DatabaseManager import DataBase
from random import choice
from string import ascii_uppercase
import json

from Logic.Player import Players
from Packets.Messages.Server.Alliance.My_Alliance_Message import MyAllianceMessage
from Packets.Messages.Server.Alliance.Events.AllianceLeaveOkMessage import AllianceLeaveOkMessage
from Packets.Messages.Server.Alliance.Alliance_Chat_Server_Message import AllianceChatServerMessage
from Packets.Messages.Server.Alliance.Alliance_Data_Message import AllianceDataMessage

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
        DataBase.loadClub(self, self.player.club_low_id)

        if self.clubmembercount == 1:
            DataBase.AddMember(self, self.player.club_low_id, self.player.low_id, self.player.name, 0)

        else:
            DataBase.AddMember(self, self.player.club_low_id, self.player.low_id, self.player.name, 2)
            DataBase.Addmsg(self, self.player.club_low_id, 4, 0, self.player.low_id, self.player.name, self.player.club_role, 4)

        # Info
        
        AllianceLeaveOkMessage(self.client, self.player).send()
        MyAllianceMessage(self.client, self.player, 0).send()
        for player in self.plrids:
            if player != self.player.low_id:
                AllianceDataMessage(self.client, self.player, 0, self.player.club_low_id).sendWithLowID(player)
                AllianceChatServerMessage(self.client, self.player, 4).sendWithLowID(player)

        DataBase.replaceValue(self, 'clubID', 0)
        self.player.club_low_id = 0
        DataBase.replaceValue(self, 'clubRole', 0)
        self.player.club_role = 0