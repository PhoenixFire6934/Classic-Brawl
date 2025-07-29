import random
import json
from Files.CsvLogic.Characters import Characters


class LogicBoxData:
    def __init__(self, player_object):
        self.player = player_object

        try:
            with open('config.json', 'r') as f:
                self.config = json.load(f)
        except FileNotFoundError:
            print("ERROR: config.json not found! Please ensure it's in the same directory.")
            self.config = {}

        self.trophy_road_brawlers_in_boxes_enabled = self.config.get('TrophyRoadBrawlersInBoxesEnabled', True)

        characters_loader = Characters()
        self.all_brawlers_data = characters_loader.get_all_brawlers_data()

        self.brawler_data_headers = []
        if self.all_brawlers_data:
            self.brawler_data_headers = self.all_brawlers_data[0]

        self.ITEM_NAME_COL_INDEX = 3
        self.HERO_TYPE_COL_INDEX = 20
        self.NAME_COL_INDEX = 0

        self.trophy_road_brawlers_item_names = [
            "shelly", "colt", "bull", "nita", "jessie", "dynamike", "brock", "tick", "8bit", "emz", "bo"
        ]

        self._brawler_item_name_to_id_map = {}
        self._brawler_id_to_item_name_map = {}

        for i, brawler_row in enumerate(self.all_brawlers_data):
            if i == 0:
                continue

            brawler_numerical_id = i - 1

            if len(brawler_row) > max(self.NAME_COL_INDEX, self.ITEM_NAME_COL_INDEX, self.HERO_TYPE_COL_INDEX):
                brawler_item_name = brawler_row[self.ITEM_NAME_COL_INDEX]
                brawler_type = brawler_row[self.HERO_TYPE_COL_INDEX]

                if brawler_type == 'Hero':
                    if brawler_item_name not in self._brawler_item_name_to_id_map:
                        self._brawler_item_name_to_id_map[brawler_item_name] = brawler_numerical_id

                    self._brawler_id_to_item_name_map[brawler_numerical_id] = brawler_item_name

    def randomize(self, box_type):

        self.box_rewards = {'Rewards': []}

        unlocked_brawlers_item_names = set()
        for b_id in self.player.brawlers_unlocked:
            item_name = self._brawler_id_to_item_name_map.get(b_id)
            if item_name:
                unlocked_brawlers_item_names.add(item_name)

        locked_brawlers_pool_item_names = []
        data_rows_for_loop = self.all_brawlers_data[1:] if len(self.all_brawlers_data) > 1 else []

        for brawler_row in data_rows_for_loop:
            if len(brawler_row) > max(self.NAME_COL_INDEX, self.ITEM_NAME_COL_INDEX, self.HERO_TYPE_COL_INDEX):
                brawler_item_name = brawler_row[self.ITEM_NAME_COL_INDEX]
                brawler_hero_type = brawler_row[self.HERO_TYPE_COL_INDEX]

                if brawler_hero_type == 'Hero' and \
                        brawler_item_name not in unlocked_brawlers_item_names:
                    if not self.trophy_road_brawlers_in_boxes_enabled and brawler_item_name in self.trophy_road_brawlers_item_names:
                        continue

                    if brawler_item_name not in locked_brawlers_pool_item_names:
                        locked_brawlers_pool_item_names.append(brawler_item_name)

        if (box_type == 10):
            check_brawler_drop = False

            if (random.randint(0, 100) < 20):
                if locked_brawlers_pool_item_names:
                    chosen_brawler_item_name = random.choice(locked_brawlers_pool_item_names)
                    brawler_id = self._brawler_item_name_to_id_map.get(chosen_brawler_item_name)

                    if brawler_id is not None:
                        brawler_reward = {'Amount': 1, 'DataRef': [16, brawler_id], 'Value': 1}
                        self.box_rewards['Rewards'].append(brawler_reward)

                        if brawler_id not in self.player.brawlers_unlocked:
                            self.player.brawlers_unlocked.append(brawler_id)
                            self.player.db.update_player_account(self.player.token, 'UnlockedBrawlers',
                                                                 self.player.brawlers_unlocked)
                            check_brawler_drop = True
                    else:
                        print(
                            f"ERROR: Small Box - Could not find canonical ID for brawler ItemName: {chosen_brawler_item_name}")

            if (random.randint(0, 100) < 100) and not check_brawler_drop:
                gold_value = random.randint(20, 100)
                gold_reward = {'Amount': gold_value, 'DataRef': [0, 0], 'Value': 7}
                self.box_rewards['Rewards'].append(gold_reward)
                found_gold_resource = False
                for resource in self.player.resources:
                    if resource['ID'] == 8:
                        resource['Amount'] += gold_value
                        found_gold_resource = True
                        break
                if found_gold_resource:
                    self.player.db.update_player_account(self.player.token, 'Resources', self.player.resources)
                else:
                    print("ERROR: Small Box - Gold resource (ID 8) not found in player.resources. Cannot update gold.")

                rewarded_brawler_ids = set()
                num_pp_rewards = 1
                for x in range(num_pp_rewards):
                    pp_value = random.randint(5, 30)
                    available_brawlers_for_pp = list(set(self.player.brawlers_unlocked) - rewarded_brawler_ids)
                    if available_brawlers_for_pp:
                        brawler_id_for_pp = random.choice(available_brawlers_for_pp)

                        if (self.player.brawlers_level.get(str(brawler_id_for_pp), 0) < 8):
                            pp_reward = {'Amount': pp_value, 'DataRef': [16, brawler_id_for_pp], 'Value': 6}
                            self.box_rewards['Rewards'].append(pp_reward)
                            self.player.brawlers_powerpoints[
                                str(brawler_id_for_pp)] = self.player.brawlers_powerpoints.get(str(brawler_id_for_pp),
                                                                                               0) + pp_value
                            self.player.db.update_player_account(self.player.token, 'BrawlersPowerPoints',
                                                                 self.player.brawlers_powerpoints)
                            rewarded_brawler_ids.add(brawler_id_for_pp)

            if (random.randint(0, 100) < 20) and not check_brawler_drop:
                if locked_brawlers_pool_item_names:
                    chosen_brawler_item_name = random.choice(locked_brawlers_pool_item_names)
                    brawler_id = self._brawler_item_name_to_id_map.get(chosen_brawler_item_name)

                    if brawler_id is not None:
                        brawler_reward = {'Amount': 1, 'DataRef': [16, brawler_id], 'Value': 1}
                        self.box_rewards['Rewards'].append(brawler_reward)

                        if brawler_id not in self.player.brawlers_unlocked:
                            self.player.brawlers_unlocked.append(brawler_id)
                            self.player.db.update_player_account(self.player.token, 'UnlockedBrawlers',
                                                                 self.player.brawlers_unlocked)
                    else:
                        print(
                            f"ERROR: Small Box - Could not find canonical ID for brawler ItemName: {chosen_brawler_item_name}")

            if (random.randint(0, 100) < 30):
                bonus = random.choice([2, 8])
                bonus_value = 0
                if (bonus == 8):
                    bonus_value = random.randint(5, 15)
                    self.player.gems = self.player.gems + bonus_value
                    self.player.db.update_player_account(self.player.token, 'Gems', self.player.gems)
                else:
                    bonus_value = random.randint(20, 50)
                    found_tokens_resource = False
                    for resource in self.player.resources:
                        if resource['ID'] == 2:
                            resource['Amount'] += bonus_value
                            found_tokens_resource = True
                            break
                    if found_tokens_resource:
                        self.player.db.update_player_account(self.player.token, 'Resources', self.player.resources)
                    else:
                        self.player.token_doubler = self.player.token_doubler + bonus_value
                        self.player.db.update_player_account(self.player.token, 'TokenDoubler',
                                                             self.player.token_doubler)
                        print(
                            f"WARN: Small Box - Could not find resource with ID 2 for Token Doublers in player.resources. Updated player.token_doubler instead.")

                bonus_reward = {'Amount': bonus_value, 'DataRef': [0, 0], 'Value': bonus}
                self.box_rewards['Rewards'].append(bonus_reward)

        elif (box_type == 12):
            if (random.randint(0, 100) < 100):
                gold_value = random.randint(50, 150)
                gold_reward = {'Amount': gold_value, 'DataRef': [0, 0], 'Value': 7}
                self.box_rewards['Rewards'].append(gold_reward)

                found_gold_resource = False
                for resource in self.player.resources:
                    if resource['ID'] == 8:
                        resource['Amount'] += gold_value
                        found_gold_resource = True
                        break
                if found_gold_resource:
                    self.player.db.update_player_account(self.player.token, 'Resources', self.player.resources)
                else:
                    print("ERROR: Big Box - Gold resource (ID 8) not found in player.resources. Cannot update gold.")

                rewarded_brawler_ids = set()
                if len(self.player.brawlers_unlocked) in [1, 2]:
                    num_pp_rewards = len(self.player.brawlers_unlocked)
                else:
                    num_pp_rewards = random.choice([2, 3])

                for x in range(num_pp_rewards):
                    pp_value = random.randint(30, 50)
                    available_brawlers_for_pp = list(set(self.player.brawlers_unlocked) - rewarded_brawler_ids)
                    if available_brawlers_for_pp:
                        brawler_id_for_pp = random.choice(available_brawlers_for_pp)
                        if (self.player.brawlers_level.get(str(brawler_id_for_pp), 0) < 8):
                            pp_reward = {'Amount': pp_value, 'DataRef': [16, brawler_id_for_pp], 'Value': 6}
                            self.box_rewards['Rewards'].append(pp_reward)
                            self.player.brawlers_powerpoints[
                                str(brawler_id_for_pp)] = self.player.brawlers_powerpoints.get(str(brawler_id_for_pp),
                                                                                               0) + pp_value
                            self.player.db.update_player_account(self.player.token, 'BrawlersPowerPoints',
                                                                 self.player.brawlers_powerpoints)
                            rewarded_brawler_ids.add(brawler_id_for_pp)

            if (random.randint(0, 100) < 35):
                if locked_brawlers_pool_item_names:
                    chosen_brawler_item_name = random.choice(locked_brawlers_pool_item_names)
                    brawler_id = self._brawler_item_name_to_id_map.get(chosen_brawler_item_name)

                    if brawler_id is not None:
                        brawler_reward = {'Amount': 1, 'DataRef': [16, brawler_id], 'Value': 1}
                        self.box_rewards['Rewards'].append(brawler_reward)

                        if brawler_id not in self.player.brawlers_unlocked:
                            self.player.brawlers_unlocked.append(brawler_id)
                            self.player.db.update_player_account(self.player.token, 'UnlockedBrawlers',
                                                                 self.player.brawlers_unlocked)
                    else:
                        print(
                            f"ERROR: Big Box - Could not find canonical ID for brawler ItemName: {chosen_brawler_item_name}")

            if (random.randint(0, 100) < 40):
                bonus = random.choice([2, 8])
                bonus_value = 0
                if (bonus == 8):
                    bonus_value = random.randint(10, 20)
                    self.player.gems = self.player.gems + bonus_value
                    self.player.db.update_player_account(self.player.token, 'Gems', self.player.gems)
                else:
                    bonus_value = random.randint(40, 80)
                    found_tokens_resource = False
                    for resource in self.player.resources:
                        if resource['ID'] == 2:
                            resource['Amount'] += bonus_value
                            found_tokens_resource = True
                            break
                    if found_tokens_resource:
                        self.player.db.update_player_account(self.player.token, 'Resources', self.player.resources)
                    else:
                        self.player.token_doubler = self.player.token_doubler + bonus_value
                        self.player.db.update_player_account(self.player.token, 'TokenDoubler',
                                                             self.player.token_doubler)
                        print(
                            f"WARN: Big Box - Could not find resource with ID 2 for Token Doublers in player.resources. Updated player.token_doubler instead.")

                bonus_reward = {'Amount': bonus_value, 'DataRef': [0, 0], 'Value': bonus}
                self.box_rewards['Rewards'].append(bonus_reward)

        elif (box_type == 11):
            if (random.randint(0, 100) < 100):
                gold_value = random.randint(100, 500)
                gold_reward = {'Amount': gold_value, 'DataRef': [0, 0], 'Value': 7}
                self.box_rewards['Rewards'].append(gold_reward)
                found_gold_resource = False
                for resource in self.player.resources:
                    if resource['ID'] == 8:
                        resource['Amount'] += gold_value
                        found_gold_resource = True
                        break
                if found_gold_resource:
                    self.player.db.update_player_account(self.player.token, 'Resources', self.player.resources)
                else:
                    print("ERROR: Mega Box - Gold resource (ID 8) not found in player.resources. Cannot update gold.")

                rewarded_brawler_ids = set()
                if len(self.player.brawlers_unlocked) in [1, 2, 3, 4]:
                    num_pp_rewards = len(self.player.brawlers_unlocked)
                else:
                    num_pp_rewards = random.choice([4, 5])

                for x in range(num_pp_rewards):
                    pp_value = random.randint(50, 150)
                    available_brawlers_for_pp = list(set(self.player.brawlers_unlocked) - rewarded_brawler_ids)
                    if available_brawlers_for_pp:
                        brawler_id_for_pp = random.choice(available_brawlers_for_pp)
                        if (self.player.brawlers_level.get(str(brawler_id_for_pp), 0) < 8):
                            pp_reward = {'Amount': pp_value, 'DataRef': [16, brawler_id_for_pp], 'Value': 6}
                            self.box_rewards['Rewards'].append(pp_reward)
                            self.player.brawlers_powerpoints[
                                str(brawler_id_for_pp)] = self.player.brawlers_powerpoints.get(str(brawler_id_for_pp),
                                                                                               0) + pp_value
                            self.player.db.update_player_account(self.player.token, 'BrawlersPowerPoints',
                                                                 self.player.brawlers_powerpoints)
                            rewarded_brawler_ids.add(brawler_id_for_pp)

            if (random.randint(0, 100) < 55):
                if locked_brawlers_pool_item_names:
                    chosen_brawler_item_name = random.choice(locked_brawlers_pool_item_names)
                    brawler_id = self._brawler_item_name_to_id_map.get(chosen_brawler_item_name)

                    if brawler_id is not None:
                        brawler_reward = {'Amount': 1, 'DataRef': [16, brawler_id], 'Value': 1}
                        self.box_rewards['Rewards'].append(brawler_reward)

                        if brawler_id not in self.player.brawlers_unlocked:
                            self.player.brawlers_unlocked.append(brawler_id)
                            self.player.db.update_player_account(self.player.token, 'UnlockedBrawlers',
                                                                 self.player.brawlers_unlocked)
                    else:
                        print(
                            f"ERROR: Mega Box - Could not find canonical ID for brawler ItemName: {chosen_brawler_item_name}")

            if (random.randint(0, 100) < 50):
                bonus = random.choice([2, 8])
                bonus_value = 0
                if (bonus == 8):
                    bonus_value = random.randint(10, 50)
                    self.player.gems = self.player.gems + bonus_value
                    self.player.db.update_player_account(self.player.token, 'Gems', self.player.gems)
                else:
                    bonus_value = random.randint(100, 400)
                    found_tokens_resource = False
                    for resource in self.player.resources:
                        if resource['ID'] == 2:
                            resource['Amount'] += bonus_value
                            found_tokens_resource = True
                            break
                    if found_tokens_resource:
                        self.player.db.update_player_account(self.player.token, 'Resources', self.player.resources)
                    else:
                        self.player.token_doubler = self.player.token_doubler + bonus_value
                        self.player.db.update_player_account(self.player.token, 'TokenDoubler',
                                                             self.player.token_doubler)
                        print(
                            f"WARN: Mega Box - Could not find resource with ID 2 for Token Doublers in player.resources. Updated player.token_doubler instead.")

                bonus_reward = {'Amount': bonus_value, 'DataRef': [0, 0], 'Value': bonus}
                self.box_rewards['Rewards'].append(bonus_reward)

        return self.box_rewards