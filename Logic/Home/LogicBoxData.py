import random

class LogicBoxData:
    def __init__(self):
        self.player = None
        self.box_rewards = {}
    
    TrophyRoadBrawlers = [0, 1, 2, 3, 7, 8, 9, 14, 22, 27, 30] # Brawlers that won't drop. The sprout was removed because its logic is not present in the game client.
    
    # common - 0, rare - 1, super_rare - 2, epic - 3, mega_epic - 4, legendary - 5
    BrawlerRarities = {
        0: 0,   # shelly
        1: 0,   # colt
        2: 0,   # bull
        3: 0,   # brok
        4: 2,   # rico
        5: 5,   # spike
        6: 1,   # barley
        7: 0,   # jessie
        8: 0,   # nita
        9: 0,   # Dynamike
        10: 1,  # El Primo
        11: 4,  # Mortis
        12: 5,  # Crow
        13: 1,  # Poco
        14: 0,  # Bo
        15: 3,  # Piper
        16: 3,  # Pam
        17: 4,  # Tara
        18: 2,  # Darryl
        19: 2,  # Penny
        20: 3,  # Frank
        21: 4,  # Gene
        22: 0,  # Tik 
        23: 5,  # Leon
        24: 1,  # Rosa
        25: 2,  # Carl
        26: 3,  # Bibi
        27: 0,  # 8bit
        28: 5,  # Sandy
        29: 3,  # Bea
        30: 0,  # Emz
        31: 4,  # Mr. P
        32: 4,  # Max
        33: 0,  # test (idk)
        34: 2,  # Jacky
        35: 0,  # test2 (idk)
        36: 0   # sprout
    }

    # chances for boxes (%, 0 - 100)
    BoxRarityChances = {
        10: {  # Brawl Box
            0: 0,  # common 
            1: 30, # rare
            2: 20,  # super rare
            3: 5,  # epic
            4: 2,  # mythic
            5: 1,  # legendary
        },
        12: {  # Big Box
            0: 0,  # common 
            1: 30, # rare
            2: 25,  # super rare
            3: 6,  # epic
            4: 4,  # mythic
            5: 2,  # legendary
        },
        11: {  # Mega Box
            0: 0,  # common 
            1: 45, # rare
            2: 30,  # super rare
            3: 10,  # epic
            4: 6,  # mythic
            5: 3,  # legendary
        }
    }
    
    def get_brawler_by_rarity(self, locked_brawlers, rarity):
        return [b for b in locked_brawlers if self.BrawlerRarities.get(b, 0) == rarity]
    
    def try_unlock_brawler(self, box_type):
        locked_brawlers = sorted(set(self.player.brawlers_id) - set(self.player.brawlers_unlocked))
    
        print(f"[DEBUG] All brawlers_id: {self.player.brawlers_id}")
        print(f"[DEBUG] Unlocked: {self.player.brawlers_unlocked}")
        print(f"[DEBUG] Locked (before filter): {locked_brawlers}")
    
        locked_brawlers = [b for b in locked_brawlers if b not in self.TrophyRoadBrawlers]
    
        print(f"[DEBUG] TrophyRoadBrawlers (excluded): {self.TrophyRoadBrawlers}")
        print(f"[DEBUG] Locked (after filter): {locked_brawlers}")
    
        if not locked_brawlers:
            print("[DEBUG] No brawlers available to unlock!")
            return None
    
        chances = self.BoxRarityChances.get(box_type, {})
    
        for rarity in [5, 4, 3, 2, 1, 0]:  # Legendary -> Common
            chance = chances.get(rarity, 0)
            print(f"[DEBUG] Trying rarity {rarity}, chance={chance}%")
            if random.randint(0, 100) < chance:
                available = self.get_brawler_by_rarity(locked_brawlers, rarity)
                print(f"[DEBUG] Available brawlers of rarity {rarity}: {available}")
                if available:
                    chosen = random.choice(available)
                    print(f"[DEBUG] >>> CHOSEN BRAWLER ID: {chosen} <<<")
                    return chosen
            else:
                print(f"[DEBUG] Rarity {rarity} failed (random > {chance})")
    
        print("[DEBUG] No brawler unlocked (all rarities failed)")
        return None

    def randomize(self, type):
        self.box_rewards = { 'Rewards': [] }

        if (type == 10):  # Brawl Box
            check = False

            if not check:
                gold_value = random.randint(20, 100)
                gold_reward = {'Amount': gold_value, 'DataRef': [0, 0], 'Value': 7}
                self.box_rewards['Rewards'].append(gold_reward)
                self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + gold_value
                self.player.db.update_player_account(self.player.token, 'Resources', self.player.resources)
                rewarded = []
                for x in range(1):
                    pp_value = random.randint(5, 30)
                    brawler = random.choice(sorted(set(self.player.brawlers_unlocked) - set(rewarded)))
                    if (self.player.brawlers_level.get(str(brawler), 0) < 8):
                        pp_reward = {'Amount': pp_value, 'DataRef': [16, brawler], 'Value': 6}
                        self.box_rewards['Rewards'].append(pp_reward)
                        self.player.brawlers_powerpoints[str(brawler)] = self.player.brawlers_powerpoints.get(str(brawler), 0) + pp_value
                        self.player.db.update_player_account(self.player.token, 'BrawlersPowerPoints', self.player.brawlers_powerpoints)
                        rewarded.append(brawler)

            brawler = self.try_unlock_brawler(type)
            if brawler:
                brawler_reward = {'Amount': 1, 'DataRef': [16, brawler], 'Value': 1}
                self.box_rewards['Rewards'].append(brawler_reward)
                if brawler not in self.player.brawlers_unlocked:
                    self.player.brawlers_unlocked.append(brawler)
                    self.player.db.update_player_account(self.player.token, 'UnlockedBrawlers', self.player.brawlers_unlocked)
                    
                    self.player.brawlers_trophies[str(brawler)] = 0
                    self.player.brawlers_high_trophies[str(brawler)] = 0
                    self.player.brawlers_level[str(brawler)] = 0
                    self.player.brawlers_powerpoints[str(brawler)] = 0
                    
                    self.player.db.update_player_account(self.player.token, 'BrawlersTrophies', self.player.brawlers_trophies)
                    self.player.db.update_player_account(self.player.token, 'BrawlersHighestTrophies', self.player.brawlers_high_trophies)
                    self.player.db.update_player_account(self.player.token, 'BrawlersLevel', self.player.brawlers_level)
                    self.player.db.update_player_account(self.player.token, 'BrawlersPowerPoints', self.player.brawlers_powerpoints)
                check = True
            
            if random.randint(0, 100) < 30:
                bonus = random.choice([2, 8])
                if bonus == 8:
                    bonus_value = random.randint(5, 15)
                    self.player.gems = self.player.gems + bonus_value
                    self.player.db.update_player_account(self.player.token, 'Gems', self.player.gems)
                else:
                    bonus_value = random.randint(20, 50)
                    self.player.token_doubler = self.player.token_doubler + bonus_value
                    self.player.db.update_player_account(self.player.token, 'TokenDoubler', self.player.token_doubler)
                bonus_reward = {'Amount': bonus_value, 'DataRef': [0, 0], 'Value': bonus}
                self.box_rewards['Rewards'].append(bonus_reward)

        elif (type == 12):  # Big Box
            gold_value = random.randint(50, 150)
            gold_reward = {'Amount': gold_value, 'DataRef': [0, 0], 'Value': 7}
            self.box_rewards['Rewards'].append(gold_reward)
            self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + gold_value
            self.player.db.update_player_account(self.player.token, 'Resources', self.player.resources)

            if len(self.player.brawlers_unlocked) in [1, 2]:
                rewarded = []
                for x in range(len(self.player.brawlers_unlocked)):
                    pp_value = random.randint(30, 50)
                    brawler = random.choice(sorted(set(self.player.brawlers_unlocked) - set(rewarded)))
                    if (self.player.brawlers_level.get(str(brawler), 0) < 8):
                        pp_reward = {'Amount': pp_value, 'DataRef': [16, brawler], 'Value': 6}
                        self.box_rewards['Rewards'].append(pp_reward)
                        self.player.brawlers_powerpoints[str(brawler)] = self.player.brawlers_powerpoints.get(str(brawler), 0) + pp_value
                        self.player.db.update_player_account(self.player.token, 'BrawlersPowerPoints', self.player.brawlers_powerpoints)
                        rewarded.append(brawler)
            else:
                rewarded = []
                for x in range(random.choice([2, 3])):
                    pp_value = random.randint(30, 50)
                    brawler = random.choice(sorted(set(self.player.brawlers_unlocked) - set(rewarded)))
                    if (self.player.brawlers_level.get(str(brawler), 0) < 8):
                        pp_reward = {'Amount': pp_value, 'DataRef': [16, brawler], 'Value': 6}
                        self.box_rewards['Rewards'].append(pp_reward)
                        self.player.brawlers_powerpoints[str(brawler)] = self.player.brawlers_powerpoints.get(str(brawler), 0) + pp_value
                        self.player.db.update_player_account(self.player.token, 'BrawlersPowerPoints', self.player.brawlers_powerpoints)
                        rewarded.append(brawler)

            brawler = self.try_unlock_brawler(type)
            if brawler:
                brawler_reward = {'Amount': 1, 'DataRef': [16, brawler], 'Value': 1}
                self.box_rewards['Rewards'].append(brawler_reward)
                if brawler not in self.player.brawlers_unlocked:
                    self.player.brawlers_unlocked.append(brawler)
                    self.player.db.update_player_account(self.player.token, 'UnlockedBrawlers', self.player.brawlers_unlocked)
                    
                    self.player.brawlers_trophies[str(brawler)] = 0
                    self.player.brawlers_high_trophies[str(brawler)] = 0
                    self.player.brawlers_level[str(brawler)] = 0
                    self.player.brawlers_powerpoints[str(brawler)] = 0
                    
                    self.player.db.update_player_account(self.player.token, 'BrawlersTrophies', self.player.brawlers_trophies)
                    self.player.db.update_player_account(self.player.token, 'BrawlersHighestTrophies', self.player.brawlers_high_trophies)
                    self.player.db.update_player_account(self.player.token, 'BrawlersLevel', self.player.brawlers_level)
                    self.player.db.update_player_account(self.player.token, 'BrawlersPowerPoints', self.player.brawlers_powerpoints)

            if random.randint(0, 100) < 40:
                bonus = random.choice([2, 8])
                if bonus == 8:
                    bonus_value = random.randint(10, 20)
                    self.player.gems = self.player.gems + bonus_value
                    self.player.db.update_player_account(self.player.token, 'Gems', self.player.gems)
                else:
                    bonus_value = random.randint(40, 80)
                    self.player.token_doubler = self.player.token_doubler + bonus_value
                    self.player.db.update_player_account(self.player.token, 'TokenDoubler', self.player.token_doubler)
                bonus_reward = {'Amount': bonus_value, 'DataRef': [0, 0], 'Value': bonus}
                self.box_rewards['Rewards'].append(bonus_reward)

        elif (type == 11):  # Mega Box
            gold_value = random.randint(100, 500)
            gold_reward = {'Amount': gold_value, 'DataRef': [0, 0], 'Value': 7}
            self.box_rewards['Rewards'].append(gold_reward)
            self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + gold_value
            self.player.db.update_player_account(self.player.token, 'Resources', self.player.resources)

            if len(self.player.brawlers_unlocked) in [1, 2, 3, 4]:
                rewarded = []
                for x in range(len(self.player.brawlers_unlocked)):
                    pp_value = random.randint(50, 150)
                    brawler = random.choice(sorted(set(self.player.brawlers_unlocked) - set(rewarded)))
                    if (self.player.brawlers_level.get(str(brawler), 0) < 8):
                        pp_reward = {'Amount': pp_value, 'DataRef': [16, brawler], 'Value': 6}
                        self.box_rewards['Rewards'].append(pp_reward)
                        self.player.brawlers_powerpoints[str(brawler)] = self.player.brawlers_powerpoints.get(str(brawler), 0) + pp_value
                        self.player.db.update_player_account(self.player.token, 'BrawlersPowerPoints', self.player.brawlers_powerpoints)
                        rewarded.append(brawler)
            else:
                rewarded = []
                for x in range(random.choice([4, 5])):
                    pp_value = random.randint(50, 150)
                    brawler = random.choice(sorted(set(self.player.brawlers_unlocked) - set(rewarded)))
                    if (self.player.brawlers_level.get(str(brawler), 0) < 8):
                        pp_reward = {'Amount': pp_value, 'DataRef': [16, brawler], 'Value': 6}
                        self.box_rewards['Rewards'].append(pp_reward)
                        self.player.brawlers_powerpoints[str(brawler)] = self.player.brawlers_powerpoints.get(str(brawler), 0) + pp_value
                        self.player.db.update_player_account(self.player.token, 'BrawlersPowerPoints', self.player.brawlers_powerpoints)
                        rewarded.append(brawler)
            
            brawler = self.try_unlock_brawler(type)
            if brawler:
                brawler_reward = {'Amount': 1, 'DataRef': [16, brawler], 'Value': 1}
                self.box_rewards['Rewards'].append(brawler_reward)
                if brawler not in self.player.brawlers_unlocked:
                    self.player.brawlers_unlocked.append(brawler)
                    self.player.db.update_player_account(self.player.token, 'UnlockedBrawlers', self.player.brawlers_unlocked)
                    
                    self.player.brawlers_trophies[str(brawler)] = 0
                    self.player.brawlers_high_trophies[str(brawler)] = 0
                    self.player.brawlers_level[str(brawler)] = 0
                    self.player.brawlers_powerpoints[str(brawler)] = 0
                    
                    self.player.db.update_player_account(self.player.token, 'BrawlersTrophies', self.player.brawlers_trophies)
                    self.player.db.update_player_account(self.player.token, 'BrawlersHighestTrophies', self.player.brawlers_high_trophies)
                    self.player.db.update_player_account(self.player.token, 'BrawlersLevel', self.player.brawlers_level)
                    self.player.db.update_player_account(self.player.token, 'BrawlersPowerPoints', self.player.brawlers_powerpoints)

            if random.randint(0, 100) < 50:
                bonus = random.choice([2, 8])
                if bonus == 8:
                    bonus_value = random.randint(10, 50)
                    self.player.gems = self.player.gems + bonus_value
                    self.player.db.update_player_account(self.player.token, 'Gems', self.player.gems)
                else:
                    bonus_value = random.randint(100, 400)
                    self.player.token_doubler = self.player.token_doubler + bonus_value
                    self.player.db.update_player_account(self.player.token, 'TokenDoubler', self.player.token_doubler)
                bonus_reward = {'Amount': bonus_value, 'DataRef': [0, 0], 'Value': bonus}
                self.box_rewards['Rewards'].append(bonus_reward)

        return self.box_rewards