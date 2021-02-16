from random import choice
from string import ascii_uppercase
import json
from typing import Dict
from Database.DatabaseManager import DataBase
from Logic.Player import Players
from Packets.Messages.Server.Alliance.AllianceSearchResultMessage import AllianceSearchResultMessage

from Utils.Reader import BSMessageReader


class Search_Message(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.RequestedName = self.read_string()

    def process(self):
        DataBase.CountClub(self, 1, 100, 2, 30)
        self.AllianceCount = 0
        for i in self.club_list:
            if self.RequestedName.lower() in self.club_data[self.club_list.index(i)]['name'].lower():
                self.AllianceCount += 1
        AllianceSearchResultMessage(self.client, self.player, self.RequestedName, self.AllianceCount).send()