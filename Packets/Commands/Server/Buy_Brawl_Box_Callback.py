from Utils.Writer import Writer
import random
from Database.DataBase import DataBase
from Logic.Shop import Shop

class BuyBrawlBoxCallback(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24111
        self.player = player

    def encode(self):
        reward_list = [0, 2, 3, 8]
        tokendoublerlist = [200, 400, 200, 600, 200, 200, 400, 200, 200, 400, 200, 200, 400, 600, 200, 200, 600, 400,
                            200, 600]

        reward = random.choice(reward_list)
        value = random.randrange(5, 20)
        gold_value = random.randrange(10, 50)
        total_reward = 2

        if reward == 8:
            new_gems = self.player.gems + value
            self.player.gems = new_gems
            DataBase.replaceValue(self, 'gems', new_gems)
        elif reward == 3:
            new_tickets = self.player.tickets + value
            self.player.tickets = new_tickets
            DataBase.replaceValue(self, 'tickets', new_tickets)
        elif reward == 2:
            value = random.choice(tokendoublerlist)
            new_tokens = self.player.tokens + value
            self.player.tokens = new_tokens
            DataBase.replaceValue(self, 'tokens', new_tokens)
        elif reward == 0:
            total_reward = 1
            value = 0

        new_gold = self.player.gold + gold_value
        self.player.gold = new_gold
        DataBase.replaceValue(self, 'gold', new_gold)

        if self.player.box_id == 3:
            new_gems = self.player.gems - Shop.boxes[1]['Cost']
            self.player.gems = new_gems
            DataBase.replaceValue(self, 'gems', new_gems)
        elif self.player.box_id == 1:
            new_gems = self.player.gems - Shop.boxes[0]['Cost']
            self.player.gems = new_gems
            DataBase.replaceValue(self, 'gems', new_gems)

        def get_id(id):
            if id == 5:   # Brawl Box
                return 10
            elif id == 4: # Big Box
                return 12
            elif id == 3: # Shop Mega Box
                return 11
            elif id == 1: # Shop Big Box
                return 12


        # Box Info
        self.writeVint(203) # Command ID
        self.writeVint(0)
        self.writeVint(1)
        self.writeVint(get_id(self.player.box_id))  # Box ID

        # Reward Count
        self.writeVint(total_reward)

        # Gold
        self.writeVint(gold_value)
        self.writeVint(0)
        self.writeVint(7) # Reward ID

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(value)
        self.writeVint(1)
        self.writeVint(0)
        self.writeVint(reward)

        for i in range(14):
            self.writeVint(0)


