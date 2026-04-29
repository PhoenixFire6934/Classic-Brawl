import sys
import pymongo
import datetime
from DataBase.MongoUtils import MongoUtils
import json
from Utils.Helpers import Helpers


class MongoDB:
    def __init__(self, conn_str):
        self.client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)
        try:
            print(f"{Helpers.cyan}[DEBUG] Connecting to Mongo DataBase...")
            self.client.server_info()
        except Exception as e:
            print(f"{Helpers.red}[ERROR] Unable to connect to Mongo server! Error: {e}")
            sys.exit()

        self.database = self.client['Classic-Brawl']
        self.players = self.database['Players']
        self.clubs = self.database['Clubs']
        self.mongo_utils = MongoUtils()

        with open('config.json', 'r') as f:
            self.config = json.load(f)

        self.data = {
            'Name': 'Guest',
            'NameSet': False,
            'Gems': self.config['Gems'],
            'Trophies': self.config['Trophies'],
            'Tickets': self.config['Tickets'],
            'Resources': [
                {'ID': 1, 'Amount': self.config['BrawlBoxTokens']},
                {'ID': 8, 'Amount': self.config['Gold']},
                {'ID': 9, 'Amount': self.config['BigBoxTokens']},
                {'ID': 10, 'Amount': self.config['StarPoints']}
            ],
            'TokenDoubler': 0,
            'HighestTrophies': self.config['Trophies'],
            'HomeBrawler': 0,
            'TrophyRoadReward': 1,
            'ExperiencePoints': self.config['ExperiencePoints'],
            'ProfileIcon': 0,
            'NameColor': 0,
            'UnlockedBrawlers': [0],
            'BrawlersTrophies': {},
            'BrawlersHighestTrophies': {},
            'BrawlersLevel': {},
            'BrawlersPowerPoints': {},
            'UnlockedSkins': [],
            'SelectedSkins': {},
            'SelectedBrawler': 0,
            'Region': self.config['Region'],
            'SupportedContentCreator': "Classic Brawl",
            'StarPower': None,
            'Gadget': None,
            'BrawlPassActivated': False,
            'WelcomeMessageViewed': False,
            'ClubID': 0,
            'ClubRole': 1,
            'TimeStamp': str(datetime.datetime.now())
        }

        self.club_data = {
            'Name': '',
            'Description': '',
            'Region': '',
            'BadgeID': 0,
            'Type': 0,
            'Trophies': 0,
            'RequiredTrophies': 0,
            'FamilyFriendly': 0,
            'Members': [],
            'Messages': []
        }

    def merge(self, dict1, dict2):
        return (dict1.update(dict2))

    def create_player_account(self, id, token):
        auth = {
            'ID': id,
            'Token': token,
        }
        auth.update(self.data)

        from Files.CsvLogic.Characters import Characters
        brawlers_id = Characters().get_brawlers_id()
        selected_skins = {}
        for id in brawlers_id:
            selected_skins[f"{id}"] = 0
        auth['SelectedSkins'] = selected_skins

        self.mongo_utils.insert_data(self.players, auth)

    def load_player_account(self, id, token):
        query = {"Token": token}
        result = self.mongo_utils.load_document(self.players, query)

        if result:
            for x in self.data:
                if x not in result:
                    self.update_player_account(token, x, self.data[x])

            query = {"Token": token}
            result = self.mongo_utils.load_document(self.players, query)

            return result

    def load_player_account_by_id(self, id):
        query = {"ID": id}
        result = self.mongo_utils.load_document(self.players, query)

        if result:
            return result

    def update_player_account(self, token, item, value):
        query = {"Token": token}
        self.mongo_utils.update_document(self.players, query, item, value)

    def update_all_players(self, query, item, value):
        self.mongo_utils.update_all_documents(self.players, query, item, value)

    def delete_all_players(self, args):
        self.mongo_utils.delete_all_documents(self.players, args)

    def delete_player(self, token):
        query = {"Token": token}
        self.mongo_utils.delete_document(self.players, query)

    def load_all_players(self, args):
        result = self.mongo_utils.load_all_documents(self.players, args)
        return result

    def load_all_players_sorted(self, args, element, element2: str = None):
        return self.mongo_utils.load_all_documents_sorted(self.players, args, element, element2)

    def create_club(self, id, data):
        auth = {
            'ID': id,
        }
        auth.update(data)
        self.mongo_utils.insert_data(self.clubs, auth)

    def update_club(self, id, item, value):
        query = {"ID": id}
        self.mongo_utils.update_document(self.clubs, query, item, value)

    def load_club(self, id):
        query = {"ID": id}
        result = self.mongo_utils.load_document(self.clubs, query)

        if result:
            for x in self.club_data:
                if x not in result:
                    self.update_club(id, x, self.club_data[x])

            query = {"ID": id}
            result = self.mongo_utils.load_document(self.clubs, query)

            return result

    def load_all_clubs_sorted(self, args, element):
        result = self.mongo_utils.load_all_documents_sorted(self.clubs, args, element, None)
        return result

    def load_all_clubs(self, args):
        result = self.mongo_utils.load_all_documents(self.clubs, args)
        return result

    def delete_club(self, id):
        query = {"ID": id}
        self.mongo_utils.delete_document(self.clubs, query)