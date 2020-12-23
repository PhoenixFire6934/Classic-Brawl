from Database.DataBase import DataBase
from random import choice
from string import ascii_uppercase
import json

from Logic.Player import Players
from Packets.Messages.Server.KeepAliveOkMessage import KeepAliveOkMessage
from Packets.Messages.Server.Alliance.AllianceStreamMessage import AllianceStreamMessage

from Utils.Reader import BSMessageReader


class KeepAliveMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        pass

    def process(self):
        KeepAliveOkMessage(self.client, self.player).send()
        if self.player.ClubID != 0:
            self.player.OldMessageCount = self.player.messageTick - 1
            DataBase.GetmsgCount(self, self.player.ClubID)

            if self.MessageCount > self.player.ClubMessageCount:
                self.player.ClubMessageCount = self.MessageCount
                AllianceStreamMessage(self.client, self.player, self.player.ClubID, 1).send()