from Packets.Messages.Server.Alliance.AllianceDataMessage import AllianceDataMessage
from time import daylight, sleep
from random import choice
from string import ascii_uppercase

from Packets.Messages.Server.Alliance.MyAllianceMessage import MyAllianceMessage
from Packets.Messages.Server.Alliance.AllianceStreamMessage import AllianceStreamMessage
from Packets.Messages.Server.Alliance.Events.AllianceJoinOkMessage import AllianceJoinOkMessage
from Packets.Messages.Server.Alliance.AllianceChatServerMessage import AllianceChatServerMessage

from Logic.Player import Players
from Database.DataBase import DataBase
from Utils.Reader import BSMessageReader


class Join_Message(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.ClubHighID = self.read_int()
        self.ClubLowID = self.read_int()

    def process(self):
        DataBase.replaceValue(self, 'clubRole', 1)
        DataBase.replaceValue(self, 'clubID', self.ClubLowID)
        self.player.ClubRole = 1
        self.player.ClubID = self.ClubLowID

        # Member adding
        DataBase.AddMember(self, self.ClubLowID, self.player.LowID, self.player.name, 1)
        DataBase.Addmsg(self, 4, 0, self.player.LowID, self.player.name, self.player.ClubRole, 3)

        # Info
        AllianceJoinOkMessage(self.client, self.player).send()
        MyAllianceMessage(self.client, self.player, self.ClubLowID).sendToAll()
        AllianceStreamMessage(self.client, self.player, self.ClubLowID, 0).send()
        AllianceChatServerMessage(self.client, self.player, 3).sendToOthers()