import json
from Utils.Helpers import Helpers
from Utils.Fingerprint import Fingerprint
from Files.CsvLogic.Characters import Characters
from Files.CsvLogic.Skins import Skins
from Files.CsvLogic.Cards import Cards

class Player:
    def __init__(self, device):
        self.device = device
        
        # Loading settings from config.json
        try:
            with open('config.json', 'r') as f:
                config_content = f.read()
        except FileNotFoundError:
            Helpers().create_config()
            with open('config.json', 'r') as f:
                config_content = f.read()
        
        settings = json.loads(config_content)
        
        # Store lists as instance attributes (needed for ClientAvatar and other places)
        self.skins_id = Skins().get_skins_id()
        self.brawlers_id = Characters().get_brawlers_id()
        
        # === Account Settings ===
        self.ID = 0
        self.token = None
        
        # Resources (initial values ​​from the config, then overwritten from the database)
        self.trophies = settings.get('Trophies', 0)
        self.tickets = settings.get('Tickets', 0)
        self.gems = settings.get('Gems', 0)
        self.resources = [
            {'ID': 1, 'Amount': settings.get('BrawlBoxTokens', 0)},
            {'ID': 8, 'Amount': settings.get('Gold', 0)},
            {'ID': 9, 'Amount': settings.get('BigBoxTokens', 0)},
            {'ID': 10, 'Amount': settings.get('StarPoints', 0)}
        ]
        self.high_trophies = settings.get('Trophies', 0)
        self.trophy_reward = 1
        self.exp_points = settings.get('ExperiencePoints', 0)
        self.profile_icon = 0
        self.name_color = 0
        self.selected_brawler = 0
        self.region = settings.get('Region', 'RU')
        self.content_creator = ""
        self.name_set = False
        self.name = 'Guest'
        self.map_id = 0
        self.use_gadget = True
        self.starpower = None
        self.gadget = None
        self.home_brawler = 0
        self.home_skin = 0
        self.leaderboard_type = 0
        self.leaderboard_is_global = False
        self.bp_activated = False
        self.token_doubler = 0
        self.welcome_msg_viewed = False
        
        # Server settings (from the config)
        self.theme_id = settings.get('ThemeID', 0)
        self.content_creator_codes = settings.get('ContentCreatorCodes', [])
        self.maintenance = settings.get('Maintenance', False)
        self.maintenance_time = settings.get('SecondsTillMaintenanceOver', 3600)
        self.patch = settings.get('Patch', False)
        self.patch_url = settings.get('PatchURL', '')
        self.patch_sha = Fingerprint.loadFinger("GameAssets/fingerprint.json")
        self.update_url = settings.get('UpdateURL', '')
        self.clubWarsEnabled = settings.get('ClubWarsEnabled', False)
        self.status = 0
        self.leaderboardData = []
        
        self.delivery_items = {}
        self.box_rewards = {}
        
        self.db = None
        self.battle_tick = 0
        
        # Skins
        self.unlocked_skins = []
        
        self.selected_skins = {}
        for id in self.brawlers_id:
            self.selected_skins[f"{id}"] = 0
        
        # Brawlers
        self.brawlers_unlocked = [0]
        
        self.brawlers_card_id = []
        for x in self.brawlers_unlocked:
            self.brawlers_card_id.append(Cards().get_unlock_by_brawler_id(x))
        
        self.brawlers_spg = []
        
        def_trophies = 0
        def_high_trophies = 0
        
        self.brawlers_trophies = {}
        for x in self.brawlers_id:
            self.brawlers_trophies[f'{x}'] = def_trophies
        
        self.brawlers_high_trophies = {}
        for x in self.brawlers_id:
            self.brawlers_high_trophies[f'{x}'] = def_high_trophies
        
        def_level = 0
        
        self.brawlers_level = {}
        for x in self.brawlers_id:
            self.brawlers_level[f'{x}'] = def_level
        
        def_pp = 0
        
        self.brawlers_powerpoints = {}
        for x in self.brawlers_id:
            self.brawlers_powerpoints[f'{x}'] = def_pp
        
        self.club_id = 0
        self.club_role = 0
        self.message_tick = 0
        
        self.clients = {}