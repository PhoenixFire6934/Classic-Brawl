from random import choice
from string import ascii_uppercase
import json
from typing import Dict

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
        self.AllianceCount = 0
        with open('club.db', 'r') as read_data:
            for club in read_data.readlines():

                clubData = json.loads(club)
                dict = json.loads(json.dumps(clubData))

                for name, info in dict.items():
                    if info['membercount'] > 0 and info['membercount'] < 100 and info['type'] <= 2 and self.AllianceCount <= 30:
                        if self.RequestedName.lower() in info['name'].lower():
                            self.AllianceCount += 1

        AllianceSearchResultMessage(self.client, self.player, self.RequestedName, self.AllianceCount).send()