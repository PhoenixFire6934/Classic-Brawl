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
	
	
	
	# Player info
	name = "Guest"
	profileIcon = 0
	namecolor = 0
	DoNotDistrub = 0
	brawlBoxes = settings['BrawlBoxTokens']
	bigBoxes = settings['BigBoxTokens']
	starPoints = settings['Starpoints']
	trophies = settings['Trophies']
	gems = settings['Gems']
	gold = settings['Gold']
	tickets = settings['Tickets']

	
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
	brawlers_trophies = {}

	for id in brawlers_id:
		brawlers_trophies.update({f'{id}': brawler_trophies_for_rank})

	brawlers_skins = {}

	for id in brawlers_id:
		brawlers_skins.update({f'{id}': 0})

	BattleResult = 0
	GameType = 0
	useGadget = 1
	Rank = 0
	Team = 0
	Bot1 = 0
	Bot1N = None
	Bot2 = 0
	Bot2N = None
	Bot3 = 0
	Bot3N = None
	Bot4 = 0
	Bot4N = None
	Bot5 = 0
	Bot5N = None




	def __init__(self, device):
		self.device = device
