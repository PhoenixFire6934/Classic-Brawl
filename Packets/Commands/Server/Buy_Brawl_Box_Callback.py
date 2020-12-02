from Utils.Writer import Writer
import random
from Database.DataBase import DataBase

class ServerBox(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24111
        self.player = player

    def encode(self):
        reward_list = [0, 0, 3, 2, 8, 2, 8, 8, 0, 3, 3, 0, 0, 2, 3, 0, 0, 0, 0, 3]

        if self.player.box_id == 5:
            reward = random.choice(reward_list)
            value = random.randrange(5, 20)
            GoldValue = random.randrange(10, 50)
            totalreward = 2

            if reward == 8:
                newGems = self.player.gems + value
                DataBase.replaceValue(self, 'gems', newGems)
            elif reward == 3:
                newTickets = self.player.tickets + value
                DataBase.replaceValue(self, 'tickets', newTickets)
            elif reward == 2:
                newTokensDoubler = 200
                value = newTokensDoubler
            elif reward == 0:
                totalreward = 1
                value = 0


            self.writeVint(203)
            self.writeVint(0)
            self.writeVint(1)
            self.writeVint(10) # brawl box
            self.writeVint(totalreward)

            self.writeVint(GoldValue)
            newGold = self.player.gold + GoldValue
            DataBase.replaceValue(self, 'gold', newGold)

            self.writeVint(0)
            self.writeVint(7)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(value)
            self.writeVint(1)
            self.writeVint(0)
            self.writeVint(reward)

            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(-1040385)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)


        if self.player.box_id == 4:
            tokendoublerlist = [200, 400, 200, 600, 200, 200, 400, 200, 200, 400, 200, 200, 400, 600, 200, 200, 600, 400, 200, 600]
            reward = random.choice(reward_list)
            value = random.randrange(5, 20)
            GoldValue = random.randrange(43, 500)
            totalreward = 2

            if reward == 8:
                newGems = self.player.gems + value
                DataBase.replaceValue(self, 'gems', newGems)
            elif reward == 3:
                newTickets = self.player.tickets + value
                DataBase.replaceValue(self, 'tickets', newTickets)
            elif reward == 2:
                value = random.choice(tokendoublerlist)
            elif reward == 0:
                totalreward = 1
                value = 0

            self.writeVint(203)
            self.writeVint(0)
            self.writeVint(1)
            self.writeVint(12)
            self.writeVint(totalreward)
            
            self.writeVint(GoldValue)
            newGold = self.player.gold + GoldValue
            DataBase.replaceValue(self, 'gold', newGold)

            self.writeVint(0)
            self.writeVint(7)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(value)
            self.writeVint(1)
            self.writeVint(0)
            self.writeVint(reward)

            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(-1040385)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)


        if self.player.box_id == 3:
            tokendoublerlist = [200, 400, 200, 600, 200, 200, 400, 200, 200, 400, 200, 200, 400, 600, 200, 200, 600, 400, 200, 600]
            reward = random.choice(reward_list)
            value = random.randrange(1, 20)
            GoldValue = random.randrange(100, 1200)
            totalreward = 2

            if reward == 8:
                newGems = self.player.gems + value
                newGems = self.player.gems - 80
                DataBase.replaceValue(self, 'gems', newGems)
            elif reward == 3:
                newGems = self.player.gems - 80
                newTickets = self.player.tickets + value
                DataBase.replaceValue(self, 'tickets', newTickets)
                DataBase.replaceValue(self, 'gems', newGems)
            elif reward == 2:
                newGems = self.player.gems - 80
                value = random.choice(tokendoublerlist)
                DataBase.replaceValue(self, 'gems', newGems)
            elif reward == 0:
                totalreward = 1
                value = 0
                newGems = self.player.gems - 80
                DataBase.replaceValue(self, 'gems', newGems)

            self.writeVint(203)
            self.writeVint(0)
            self.writeVint(1)
            self.writeVint(11)
            self.writeVint(totalreward)

            self.writeVint(GoldValue)
            newGold = self.player.gold + GoldValue
            DataBase.replaceValue(self, 'gold', newGold)

            self.writeVint(0)
            self.writeVint(7)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(value)
            self.writeVint(1)
            self.writeVint(0)
            self.writeVint(reward)

            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(-1040385)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)


        if self.player.box_id == 1 or self.player.box_id == 10 :
            tokendoublerlist = [200, 400, 200, 600, 200, 200, 400, 200, 200, 400, 200, 200, 400, 600, 200, 200, 600, 400, 200, 600] 
            reward = random.choice(reward_list)
            value = random.randrange(5, 20)
            GoldValue = random.randrange(43, 500)
            totalreward = 2

            if reward == 8:
                newGems = self.player.gems + value
                newGems = self.player.gems - 30
                DataBase.replaceValue(self, 'gems', newGems)
            elif reward == 3:
                newTickets = self.player.tickets + value
                newGems = self.player.gems - 30
                DataBase.replaceValue(self, 'gems', newGems)
                DataBase.replaceValue(self, 'tickets', newTickets)
            elif reward == 2:
                value = random.choice(tokendoublerlist)
                newGems = self.player.gems - 30
                DataBase.replaceValue(self, 'gems', newGems)
            elif reward == 0:
                totalreward = 1
                value = 0
                newGems = self.player.gems - 30
                DataBase.replaceValue(self, 'gems', newGems)

            self.writeVint(203)
            self.writeVint(0)
            self.writeVint(1)
            self.writeVint(12)
            self.writeVint(totalreward)
            
            self.writeVint(GoldValue)
            newGold = self.player.gold + GoldValue
            DataBase.replaceValue(self, 'gold', newGold)

            self.writeVint(0)
            self.writeVint(7)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(value)
            self.writeVint(1)
            self.writeVint(0)
            self.writeVint(reward)

            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(-1040385)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
