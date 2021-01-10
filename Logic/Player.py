import json
from Utils.Config import Config
from Utils.Fingerprint import Fingerprint
from Files.CsvLogic.Characters import Characters
from Files.CsvLogic.Skins import Skins
from Files.CsvLogic.Cards import Cards

class Players:
	try:
		config = open('config.json', 'r')
		content = config.read()
	except FileNotFoundError:
		print("Creating config.json...")
		Config.create_config()
		config = open('config.json', 'r')
		content = config.read()

	settings = json.loads(content)

	# Player data
	high_id = 0
	low_id = 0
	token = None
	box_id = 0
	map_id = 7
	room_id = 0
	brawler_id = 0
	skin_id = 0

	
	# Brawler data
	skins_id = Skins.get_skins_id()
	brawlers_id = Characters.get_brawlers_id()
	card_skills_id = Cards.get_spg_id()
	card_unlock_id = Cards.get_brawler_unlock()
	brawler_power_level = settings['BrawlerPowerLevel']
	brawler_trophies_for_rank = settings['BrawlerTrophiesForRank']
	brawler_trophies = settings['BrawlerTrophies']
	brawler_upgrade_points = settings['BrawlerUpgradePoints']
	gadget = 255
	starpower = 76

	brawlers_trophies = {}
	for id in brawlers_id:
		brawlers_trophies.update({f'{id}': brawler_trophies_for_rank})

	brawlers_skins = {}
	for id in brawlers_id:
		brawlers_skins.update({f'{id}': 0})
	
	
	
	# Player info
	name = "Guest"
	profile_icon = 0
	name_color = 0
	do_not_distrub = 0
	brawl_boxes = settings['BrawlBoxTokens']
	big_boxes = settings['BigBoxTokens']
	star_points = settings['Starpoints']
	trophies = settings['Trophies']
	gems = settings['Gems']
	gold = settings['Gold']
	tickets = settings['Tickets']
	tokens = 0

	
	# Server config
	update_url = settings['UpdateUrl']
	patch_url = settings['PatchUrl']
	patch_sha = Fingerprint.loadFinger("GameAssets/fingerprint.json")

	err_code = 7
	maintenance = False
	patch = False

	patching = settings['Patch']

	if patching:
		error_code = 7
		patch = True


	if settings['Maintenance']:
		err_code = 10
		maintenance = True
	
	
	# Chat data
	message_tick = 0
	bot_message_tick = 0


	# Friendly game data & info
	battle_result = 0
	game_type = 0
	use_gadget = 1
	rank = 0
	team = 0

	bot1 = 0
	bot1_n = None
	bot2 = 0
	bot2_n = None
	bot3 = 0
	bot3_n = None
	bot4 = 0
	bot4_n = None
	bot5 = 0
	bot5_n = None


	def __init__(self, device):
		self.device = device
