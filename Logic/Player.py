import json
import sys
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

	
	HighID = 0
	LowID = 0
	Token = None
	boxID = 0
	mapID = 7
	roomID = 0
	brawlerID = 0
	skinID = 0


	SkinsCount = Skins.get_skins_id()
	BrawlersCount = Characters.get_brawlers_id()
	CardSkillsID = Cards.get_spg_id()
	CardUnlockID = Cards.get_brawler_unlock()


	brawler_power_level = settings['BrawlerPowerLevel']
	brawler_trophies_for_rank = settings['BrawlerTrophiesForRank']
	brawler_trophies = settings['BrawlerTrophies']
	brawler_upgrade_points = settings['BrawlerUpgradePoints']
	trophies = settings['Trophies']
	gems = settings['Gems']
	gold = settings['Gold']
	tickets = settings['Tickets']
	name = "Guest"
	profileIcon = 0
	brawlBoxes = settings['BrawlBoxTokens']
	bigBoxes = settings['BigBoxTokens']
	starPoints = settings['Starpoints']


	updateUrl = settings['UpdateUrl']
	patchUrl = settings['PatchUrl']
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

	messageTick = 0
	botMessageTick = 0


	BrawlersTrophies = {
		'0':  brawler_trophies_for_rank,
		'1':  brawler_trophies_for_rank,
		'2':  brawler_trophies_for_rank,
		'3':  brawler_trophies_for_rank,
		'4':  brawler_trophies_for_rank,
		'5':  brawler_trophies_for_rank,
		'6':  brawler_trophies_for_rank,
		'7':  brawler_trophies_for_rank,
		'8':  brawler_trophies_for_rank,
		'9':  brawler_trophies_for_rank,
		'10': brawler_trophies_for_rank,
		'11': brawler_trophies_for_rank,
		'12': brawler_trophies_for_rank,
		'13': brawler_trophies_for_rank,
		'14': brawler_trophies_for_rank,
		'15': brawler_trophies_for_rank,
		'16': brawler_trophies_for_rank,
		'17': brawler_trophies_for_rank,
		'18': brawler_trophies_for_rank,
		'19': brawler_trophies_for_rank,
		'20': brawler_trophies_for_rank,
		'21': brawler_trophies_for_rank,
		'22': brawler_trophies_for_rank,
		'23': brawler_trophies_for_rank,
		'24': brawler_trophies_for_rank,
		'25': brawler_trophies_for_rank,
		'26': brawler_trophies_for_rank,
		'27': brawler_trophies_for_rank,
		'28': brawler_trophies_for_rank,
		'29': brawler_trophies_for_rank,
		'30': brawler_trophies_for_rank,
		'31': brawler_trophies_for_rank,
		'32': brawler_trophies_for_rank,
		'34': brawler_trophies_for_rank,
		'37': brawler_trophies_for_rank
	}


	shellySkin = 0
	nitaSkin = 0
	coltSkin = 0
	bullSkin = 0
	jessieSkin = 0
	brockSkin = 0
	dynamikeSkin = 0
	boSkin = 0
	elprimoSkin = 0
	barleySkin = 0
	pocoSkin = 0
	ricoSkin = 0
	darrylSkin = 0
	pennySkin = 0
	piperSkin = 0
	pamSkin = 0
	frankSkin = 0
	mortisSkin = 0
	taraSkin = 0
	spikeSkin = 0
	crowSkin = 0
	geneSkin = 0
	tickSkin = 0
	leonSkin = 0
	rosaSkin = 0
	carlSkin = 0
	bibiSkin = 0
	bitSkin = 0
	sandySkin =0
	beaSkin = 0
	emzSkin = 0
	mrpSkin = 0
	maxSkin = 0
	jackySkin =0
	galeSkin = 0
	naniSkin = 0
	sproutSkin =0
	gadget = 255
	starpower = 76
	namecolor = 12
	GameType = 0
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
	useGadget = 1
	DoNotDistrub = 0




	def __init__(self, device):
		self.device = device