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

	# Player and objects ID
	HighID = 0
	LowID = 0
	Token = None
	boxID = 0
	mapID = 7
	roomID = 0
	brawlerID = 0
	skinID = 0
	TestVal = 1

	# Brawler and skins arrays
	SkinsCount = Skins.get_skins_id()
	BrawlersCount = Characters.get_brawlers_id()
	CardSkillsID = Cards.get_spg_id()
	CardUnlockID = Cards.get_brawler_unlock()

	# General player (Brawler, Currency, etc..
	UnlockType = settings['UnlockedBrawlersOption']
	BrawlersDict = json.loads(json.dumps(settings['UnlockedBrawler'][0]))
	BrawlersUnlockedState = {}

	if UnlockType == "All":
		for i in BrawlersCount:
			BrawlersUnlockedState[str(i)] = 1

	elif UnlockType == "SpecifiedOnly":	
		index = 0
		for brawlers_name in BrawlersDict:
			BrawlersUnlockedState[str(index)] = BrawlersDict[brawlers_name]
			if index == 34:
				index += 3
			elif index == 32:
				index += 2
			else:
				index += 1

	elif UnlockType == "StarterOnly":
		starter = [0, 1, 2, 3, 7, 8, 9, 14, 22, 27, 30]
		for i in BrawlersCount:
			if i in starter:
				BrawlersUnlockedState[str(i)] = 1
			else:
				BrawlersUnlockedState[str(i)] = 0

	brawler_power_level = settings['BrawlerPowerLevel']
	brawler_trophies_for_rank = settings['BrawlerTrophiesForRank']
	brawler_trophies = settings['BrawlerTrophies']
	brawler_upgrade_points = settings['BrawlerUpgradePoints']

	brawlers_skins = {}
	for id in BrawlersCount:
		brawlers_skins.update({f'{id}': 0})

	gems = settings['Gems']
	gold = settings['Gold']
	tickets = settings['Tickets']
	highesttrophies = 0
	trophies = 0
	name = None
	profileIcon = 1
	namecolor = 5
	brawlBoxes = settings['BrawlBoxTokens']
	bigBoxes = settings['BigBoxTokens']
	starPoints = settings['Starpoints']

	# Alliances
	ClubID = 0
	ClubRole = 0
	ClubAction = 0
	ClubMessageCount = 0
	OldMessageCount = 0

	# Ignore it
	# contentCreator = None


	Resources = {
		'brawlbox': {'id': 1, 'amount': brawlBoxes},
		'gold': {'id': 8, 'amount': gold},
		'bigbox': {'id': 9, 'amount':bigBoxes},
		'starpoints': {'id': 10, 'amount': starPoints},

	}

	# Message stuff...
	updateUrl = settings['UpdateUrl']
	patchUrl = settings['PatchUrl']
	patch_sha = Fingerprint.loadFinger("GameAssets/fingerprint.json")

	err_code = 7
	maintenance = False
	patch = False
	debug = False

	patching = settings['Patch']

	if patching:
		error_code = 7
		patch = True


	if settings['Maintenance']:
		err_code = 10
		maintenance = True

	# Chat
	messageTick = 0
	botMessageTick = 0

	BrawlersTrophies = {
		'0':  brawler_trophies,
		'1':  brawler_trophies,
		'2':  brawler_trophies,
		'3':  brawler_trophies,
		'4':  brawler_trophies,
		'5':  brawler_trophies,
		'6':  brawler_trophies,
		'7':  brawler_trophies,
		'8':  brawler_trophies,
		'9':  brawler_trophies,
		'10': brawler_trophies,
		'11': brawler_trophies,
		'12': brawler_trophies,
		'13': brawler_trophies,
		'14': brawler_trophies,
		'15': brawler_trophies,
		'16': brawler_trophies,
		'17': brawler_trophies,
		'18': brawler_trophies,
		'19': brawler_trophies,
		'20': brawler_trophies,
		'21': brawler_trophies,
		'22': brawler_trophies,
		'23': brawler_trophies,
		'24': brawler_trophies,
		'25': brawler_trophies,
		'26': brawler_trophies,
		'27': brawler_trophies,
		'28': brawler_trophies,
		'29': brawler_trophies,
		'30': brawler_trophies,
		'31': brawler_trophies,
		'32': brawler_trophies,
		'34': brawler_trophies,
		'37': brawler_trophies
	}

	BrawlersTrophiesForRank = {
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

	BrawlersUpgradePoints = {
		'0':  brawler_upgrade_points,
		'1':  brawler_upgrade_points,
		'2':  brawler_upgrade_points,
		'3':  brawler_upgrade_points,
		'4':  brawler_upgrade_points,
		'5':  brawler_upgrade_points,
		'6':  brawler_upgrade_points,
		'7':  brawler_upgrade_points,
		'8':  brawler_upgrade_points,
		'9':  brawler_upgrade_points,
		'10': brawler_upgrade_points,
		'11': brawler_upgrade_points,
		'12': brawler_upgrade_points,
		'13': brawler_upgrade_points,
		'14': brawler_upgrade_points,
		'15': brawler_upgrade_points,
		'16': brawler_upgrade_points,
		'17': brawler_upgrade_points,
		'18': brawler_upgrade_points,
		'19': brawler_upgrade_points,
		'20': brawler_upgrade_points,
		'21': brawler_upgrade_points,
		'22': brawler_upgrade_points,
		'23': brawler_upgrade_points,
		'24': brawler_upgrade_points,
		'25': brawler_upgrade_points,
		'26': brawler_upgrade_points,
		'27': brawler_upgrade_points,
		'28': brawler_upgrade_points,
		'29': brawler_upgrade_points,
		'30': brawler_upgrade_points,
		'31': brawler_upgrade_points,
		'32': brawler_upgrade_points,
		'34': brawler_upgrade_points,
		'37': brawler_upgrade_points
	}

	# Brawler stats and more..
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

    # Friendly game (Teams, info, result)
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

	def CreateNewBrawlersList():
		BrawlersDict = {}
		for id in Players.BrawlersCount:
			if id == 0:
				BrawlersDict[str(id)] = 1
			else:
				BrawlersDict[str(id)] = 0
		return BrawlersDict
		
	def __init__(self, device):
		self.device = device