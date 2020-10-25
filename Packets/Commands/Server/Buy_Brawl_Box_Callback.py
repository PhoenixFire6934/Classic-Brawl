from Utils.Writer import Writer
import random
from Database.DataBase import DataBase

class ServerBox(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24111
        self.player = player

    def encode(self):
        reward_list = [2 , 3 , 8]

        if self.player.boxID == 5:

            self.writeVint(203)
            self.writeVint(0)
            self.writeVint(1)
            self.writeVint(10) # brawl box
            self.writeVint(2)
            GoldValue = random.randrange(1, 1000)
            self.writeVint(GoldValue)

            newGold = self.player.gold + GoldValue
            DataBase.replaceValue(self, 'gold', newGold)

            self.writeVint(0)
            self.writeVint(7)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            value = random.randrange(1, 20)
            self.writeVint(value)
            self.writeVint(1)
            self.writeVint(0)
            reward = random.choice(reward_list)
            self.writeVint(reward)

            if reward == 8:
                newGems = self.player.gems + value
                DataBase.replaceValue(self, 'gems', newGems)
            elif reward == 3:
                newTickets = self.player.tickets + value
                DataBase.replaceValue(self, 'tickets', newTickets)

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


        if self.player.boxID == 4:
            newBigBox = self.player.bigBoxes - 10
            DataBase.replaceValue(self, 'bigBoxes', newBigBox)
            self.writeVint(203)
            self.writeVint(0)
            self.writeVint(1)
            self.writeVint(12)
            self.writeVint(2)
            GoldValue = random.randrange(1, 2500)
            self.writeVint(GoldValue)

            newGold = self.player.gold + GoldValue
            DataBase.replaceValue(self, 'gold', newGold)

            self.writeVint(0)
            self.writeVint(7)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            value = random.randrange(1, 50)
            self.writeVint(value)
            self.writeVint(1)
            self.writeVint(0)
            reward = random.choice(reward_list)
            self.writeVint(reward)

            if reward == 8:
                newGems = self.player.gems + value
                DataBase.replaceValue(self, 'gems', newGems)
            elif reward == 3:
                newTickets = self.player.tickets + value
                DataBase.replaceValue(self, 'tickets', newTickets)

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


        if self.player.boxID == 3:
            self.writeVint(203)
            self.writeVint(0)
            self.writeVint(1)
            self.writeVint(11)
            self.writeVint(2)

            GoldValue = random.randrange(1, 5000)
            self.writeVint(GoldValue)

            newGold = self.player.gold + GoldValue
            DataBase.replaceValue(self, 'gold', newGold)

            self.writeVint(0)
            self.writeVint(7)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            value = random.randrange(1, 100)
            self.writeVint(value)
            self.writeVint(1)
            self.writeVint(0)
            reward = random.choice(reward_list)
            self.writeVint(reward)

            if reward == 8:
                newGems = self.player.gems + value - 80
                DataBase.replaceValue(self, 'gems', newGems)
            elif reward == 3:
                newTickets = self.player.tickets + value
                newGems = self.player.gems - 80
                DataBase.replaceValue(self, 'tickets', newTickets)
                DataBase.replaceValue(self, 'gems', newGems)
            else:
                newGems = self.player.gems - 80
                DataBase.replaceValue(self, 'gems', newGems)

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


        if self.player.boxID == 1 or self.player.boxID == 10 :
            self.writeVint(203)
            self.writeVint(0)
            self.writeVint(1)
            self.writeVint(12)
            self.writeVint(2)

            GoldValue = random.randrange(1, 2500)
            self.writeVint(GoldValue)

            newGold = self.player.gold + GoldValue
            DataBase.replaceValue(self, 'gold', newGold)

            self.writeVint(0)
            self.writeVint(7)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            value = random.randrange(1, 50)
            self.writeVint(value)
            self.writeVint(1)
            self.writeVint(0)
            reward = random.choice(reward_list)
            self.writeVint(reward)

            if reward == 8:
                newGems = self.player.gems + value - 30
                DataBase.replaceValue(self, 'gems', newGems)
            elif reward == 3:
                newTickets = self.player.tickets + value
                newGems = self.player.gems - 30
                DataBase.replaceValue(self, 'tickets', newTickets)
                DataBase.replaceValue(self, 'gems', newGems)
            else:
                newGems = self.player.gems - 30
                DataBase.replaceValue(self, 'gems', newGems)

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