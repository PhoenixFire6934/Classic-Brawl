import json, string, random
from colorama import Fore

class Helpers:
    connected_clients = {"ClientsCount": 0, "Clients": {}}
    
    yellow = Fore.YELLOW
    green = Fore.GREEN
    blue = Fore.LIGHTBLUE_EX
    cyan = Fore.CYAN
    red = Fore.RED
    reset = Fore.RESET
    
    @staticmethod
    def randomToken():
        lettersAndDigits = string.ascii_letters + string.digits
        return ''.join(random.choice(lettersAndDigits) for i in range(40))
    
    @staticmethod
    def randomID(length=8):
        return int(''.join([str(random.randint(0, 9)) for _ in range(length)]))
    
    @staticmethod
    def randomMapID():
        return random.randint(1, 2147483647)
    
    @staticmethod
    def get_box_type(id):
        if id == 5:    # Brawl Box
            return 10
        elif id == 4:  # Big Box
            return 12
        elif id == 3:  # Shop Mega Box
            return 11
        elif id == 1:  # Shop Big Box
            return 12
    
    @staticmethod
    def create_config():
        settings = {
            "MongoConnectionURL": "",
            "UpgradesEnabled": false,
            "ClubWarsEnabled": false,
            "StarPoints": 5000,
            "Tickets": 7000,
            "Gold": 10000,
            "Gems": 100000,
            "Trophies": 0,
            "ExperiencePoints": 999999,
            "BrawlBoxTokens": 99999,
            "BigBoxTokens": 99999,
            "Region": "RO",
            "ThemeID": 0,
            "ContentCreatorCodes": ["modern brawl"],
            "BannedIPs": [],
            "Maintenance": false,
            "SecondsTillMaintenanceOver": 3600,
            "Patch": false,
            "PatchURL": "http://192.168.0.103:8080/",
            "UpdateURL": ""
        }

        with open('config.json', 'w') as config_file:
            json.dump(settings, config_file)
    
    @staticmethod
    def load_account(player, player_data):
        """Loads data from the database (dictionary) into the Player instance"""
        player.name_set = player_data.get('NameSet', False)
        player.name = player_data.get('Name', 'Guest')
        player.trophies = player_data.get('Trophies', 0)
        player.gems = player_data.get('Gems', 0)
        player.resources = player_data.get('Resources', player.resources)
        player.token_doubler = player_data.get('TokenDoubler', 0)
        player.high_trophies = player_data.get('HighestTrophies', 0)
        player.trophy_reward = player_data.get('TrophyRoadReward', 1)
        player.exp_points = player_data.get('ExperiencePoints', 0)
        player.profile_icon = player_data.get('ProfileIcon', 0)
        player.name_color = player_data.get('NameColor', 0)
        player.brawlers_unlocked = player_data.get('UnlockedBrawlers', [0])
        player.brawlers_trophies = player_data.get('BrawlersTrophies', player.brawlers_trophies)
        player.brawlers_high_trophies = player_data.get('BrawlersHighestTrophies', player.brawlers_high_trophies)
        player.brawlers_level = player_data.get('BrawlersLevel', player.brawlers_level)
        player.brawlers_powerpoints = player_data.get('BrawlersPowerPoints', player.brawlers_powerpoints)
        player.unlocked_skins = player_data.get('UnlockedSkins', [])
        
        # Redesigned skin selection in the lobby
        player.selected_skins = player_data.get('SelectedSkins', player.selected_skins)
        selected_skins_data = player_data.get('SelectedSkins', None)
        if selected_skins_data and len(selected_skins_data) > 0:
            player.selected_skins = selected_skins_data

        player.tickets = player_data.get('Tickets', 0)
        player.home_brawler = player_data.get('SelectedBrawler', 0)
        player.region = player_data.get('Region', 'RO')
        player.content_creator = player_data.get('SupportedContentCreator', '')
        player.club_id = player_data.get('ClubID', 0)
        player.club_role = player_data.get('ClubRole', 1)
        player.starpower = player_data.get('StarPower', player.starpower)
        player.gadget = player_data.get('Gadget', player.gadget)
    
    @staticmethod
    def load_club(player, club_data):
        """Loads club data into a Player instance"""
        try:
            if club_data and club_data.get('Messages'):
                player.message_tick = club_data['Messages'][-1]['Tick']
        except:
            pass