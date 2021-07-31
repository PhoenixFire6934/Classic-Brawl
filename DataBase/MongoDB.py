import sys
import pymongo
import datetime
from DataBase.MongoUtils import MongoUtils
from Logic.Player import Player
import json
import bson
from Utils.Helpers import Helpers


class MongoDB:
    def __init__(self, conn_str):
        self.player = Player
        self.client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS = 5000)
        try:
            print(f"{Helpers.cyan}[DEBUG] Connecting to Mongo DataBase...")
            self.client.server_info()
        except Exception:
            print(f"{Helpers.red}[ERROR] Unable to connect to Mongo server!")
            sys.exit()

        self.database = self.client['Classic-Brawl']
        self.players = self.database['Players']
        self.clubs = self.database['Clubs']
        self.mongo_utils = MongoUtils()

        self.data = {
            'Name': 'Guest',
            'NameSet': False,
            'Gems': Player.gems,
            'Trophies': Player.trophies,
            'Tickets': Player.tickets,
            'Resources': Player.resources,
            'TokenDoubler': 0,
            'HighestTrophies': 0,
            'HomeBrawler': 0,
            'TrophyRoadReward': 300,
            'ExperiencePoints': Player.exp_points,
            'ProfileIcon': 0,
            'NameColor': 0,
            'UnlockedBrawlers': Player.brawlers_unlocked,
            'BrawlersTrophies': Player.brawlers_trophies,
            'BrawlersHighestTrophies': Player.brawlers_high_trophies,
            'BrawlersLevel': Player.brawlers_level,
            'BrawlersPowerPoints': Player.brawlers_powerpoints,
            'UnlockedSkins': Player.unlocked_skins,
            'SelectedSkins': Player.selected_skins,
            'SelectedBrawler': 0,
            'Region': Player.region,
            'SupportedContentCreator': "Modern Brawl",
            'StarPower': Player.starpower,
            'Gadget': Player.gadget,
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


    def load_all_players_sorted(self, args, element):
        result = self.mongo_utils.load_all_documents_sorted(self.players, args, element)

        return result


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
        result = self.mongo_utils.load_all_documents_sorted(self.clubs, args, element)

        return result

    def load_all_clubs(self, args):
        result = self.mongo_utils.load_all_documents(self.clubs, args)

        return result

    def delete_club(self, id):
        query = {"ID": id}
        self.mongo_utils.delete_document(self.clubs, query)