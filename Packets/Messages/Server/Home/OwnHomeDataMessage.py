from Files.CsvLogic.Characters import Characters
from Files.CsvLogic.Skins import Skins
from Files.CsvLogic.Cards import Cards
from datetime import datetime

from Utils.Writer import Writer
from Database.DatabaseManager import DataBase

from Logic.Shop import Shop
from Logic.EventSlots import EventSlots


class OwnHomeDataMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24101
        self.player = player

    def encode(self):
        DataBase.loadAccount(self)
        self.writeVint(0)
        self.writeVint(0)  # Timestamp

        self.writeVint(self.player.trophies)  # Player Trophies
        self.writeVint(self.player.highest_trophies)  # Player Max Reached Trophies

        self.writeVint(0)
        self.writeVint(1)  # Trophy Road Reward

        self.writeVint(99999)  # Player exp set to high number because of the name and bot battle level restriction

        self.writeScId(28, self.player.profile_icon)  # Player Icon ID

        self.writeVint(0)  # array

        # Selected Skins array
        self.writeVint(len(self.player.brawlers_skins))
        for brawler_id in self.player.brawlers_skins:
            self.writeVint(29)
            self.writeVint(self.player.brawlers_skins[brawler_id])  # skinID

        # Unlocked Skins array
        self.writeVint(len(self.player.skins_id))
        for skin_id in self.player.skins_id:
            self.writeScId(29, skin_id)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeBoolean(False)  # "token limit reached message" if true
        self.writeVint(1)
        self.writeBoolean(True)

        self.writeVint(self.player.tokensdoubler)  # Token doubler ammount
        self.writeVint(240123)  # Season End Timer

        self.writeVint(8)  # related to shop token doubler
        self.writeBoolean(True)
        self.writeBoolean(True)
        self.writeBoolean(True)

        self.writeBoolean(False) # ???

        #region Shop
        self.writeVint(1)

        self.writeVint(1)

        self.writeVint(1)
        self.writeVint(1)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(1)
        self.writeVint(1)

        self.writeVint(1)
        self.writeVint(100)
        self.writeVint(0)

        self.writeBoolean(False)
        self.writeVint(1)
        self.writeBoolean(False)
        self.writeInt(0)
        #endregion

        self.writeVint(1) # Unknow array
        self.writeVint(10)
        self.writeVint(20)
        self.writeVint(30)

        self.writeVint(200) # Battle tokens
        self.writeVint(0)  # Time till Bonus Tokens (seconds)

        self.writeVint(0)  # array

        self.writeVint(self.player.tickets)  # Tickets
        self.writeVint(0)

        self.writeScId(16, self.player.brawler_id)  # Selected Brawler

        self.writeString("RO")  # Location

        self.writeBoolean(False)

        self.writeVint(2019049)
        self.writeVint(100)
        self.writeVint(10)

        self.writeVint(30)
        self.writeVint(3)
        self.writeVint(80)

        self.writeVint(10)
        self.writeVint(50)
        self.writeVint(1000)

        self.writeVint(500)
        self.writeVint(50)
        self.writeVint(999900)

        self.writeVint(0)

        self.writeVint(8)  # array

        for i in range(8):
            self.writeVint(i)

        # Logic Events
        count = len(EventSlots.maps)
        self.writeVint(count)

        for map in EventSlots.maps:

            self.writeVint(EventSlots.maps.index(map) + 1)
            self.writeVint(EventSlots.maps.index(map) + 1)
            self.writeVint(map['Ended'])  # IsActive | 0 = Active, 1 = Disabled
            self.writeVint(EventSlots.Timer)  # Timer

            self.writeVint(0)
            self.writeScId(15, map['ID'])

            self.writeVint(map['Status'])

            self.writeString()
            self.writeVint(0)

            if map['Modifier'] > 0:
                self.writeBoolean(True)  # Gamemodifier boolean
                self.writeVint(1)  # ModifierID
            else:
                self.writeBoolean(False)

            self.writeVint(0)

        self.writeVint(0)  # array

        # Logic Shop

        self.writeVint(8)
        for i in [20, 35, 75, 140, 290, 480, 800, 1250]:
            self.writeVint(i)

        self.writeVint(8)
        for i in [1, 2, 3, 4, 5, 10, 15, 20]:
            self.writeVint(i)

        self.writeVint(3)
        for i in [10, 30, 80]:  # Tickets price
            self.writeVint(i)

        self.writeVint(3)
        for i in [6, 20, 60]:  # Tickets amount
            self.writeVint(i)

        self.writeVint(3)
        for item in Shop.gold:
            self.writeVint(item['Cost'])

        self.writeVint(3)
        for item in Shop.gold:
            self.writeVint(item['Amount'])

        self.writeVint(0)
        self.writeVint(200)  # Max Tokens
        self.writeVint(20)  # Plus Tokens

        self.writeVint(8640)
        self.writeVint(10)
        self.writeVint(5)

        self.writeVint(6)

        self.writeVint(50)
        self.writeVint(604800)

        self.writeBoolean(True)  # Box boolean

        self.writeVint(0)  # array

        self.writeVint(1)  # Menu Theme
        self.writeInt(1)
        self.writeInt(self.player.theme_id)  # Theme ID

        self.writeInt(0)
        self.writeInt(1)

        self.writeVint(0)

        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(self.player.high_id)  # High Id
        self.writeVint(self.player.low_id)  # Low Id

        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)

        if self.player.name == "Guest":
            self.writeString("Guest")  # Player Name
            self.writeVint(0)
            DataBase.createAccount(self)
        else:
            self.writeString(self.player.name)  # Player Name
            self.writeVint(1)

        self.writeString()

        self.writeVint(8)

        self.writeVint(len(self.player.card_unlock_id) + 3)

        index = 0
        for unlock_id in self.player.card_unlock_id:
            self.writeVint(23)
            self.writeVint(unlock_id)
            try:
                self.writeVint(self.player.BrawlersUnlockedState[str(index)])
            except:
                self.writeVint(1)

            if index == 21:
                index += 2
            else:
                index += 1

        self.writeVint(5)
        self.writeVint(1)
        self.writeVint(self.player.brawl_boxes) #Brawl Box tokens

        self.writeVint(5)
        self.writeVint(8)
        self.writeVint(self.player.gold) #Gold

        self.writeVint(5)
        self.writeVint(9)
        self.writeVint(self.player.big_boxes) #Big Box tokens

        # Brawlers Trophies array
        self.writeVint(len(self.player.brawlers_id))  # brawlers count

        for brawler_id in self.player.brawlers_id:
            self.writeScId(16, brawler_id)
            self.writeVint(self.player.brawlers_trophies[str(brawler_id)])

        # Brawlers Trophies for Rank array
        self.writeVint(len(self.player.brawlers_id))  # brawlers count

        for brawler_id in self.player.brawlers_id:
            self.writeScId(16, brawler_id)
            self.writeVint(self.player.brawlers_trophies_in_rank[str(brawler_id)])

        self.writeVint(0)  # array

        # Brawlers Upgrade Points array
        self.writeVint(len(self.player.brawlers_id))  # brawlers count

        for brawler_id in self.player.brawlers_id:
            self.writeScId(16, brawler_id)
            self.writeVint(self.player.brawlers_upgradium[str(brawler_id)])

        # Brawlers Power Level array
        self.writeVint(len(self.player.brawlers_id))  # brawlers count

        for brawler_id in self.player.brawlers_id:
            self.writeScId(16, brawler_id)
            self.writeVint(self.player.Brawler_level[str(brawler_id)])

        # Gadgets and Star Powers array
        spgList = []
        for id, level in self.player.Brawler_level.items():
            if level == 8:
                spg = Cards.get_unlocked_spg(self, int(id))
                for i in range(len(spg)):
                    spgList.append(spg[i])

        self.writeVint(len(self.player.card_skills_id))  # count

        for skill_id in self.player.card_skills_id:
            self.writeVint(23)
            self.writeVint(skill_id)
            if skill_id in spgList:
                self.writeVint(1)
            else:
                self.writeVint(0)

        # "new" Brawler Tag array
        self.writeVint(0)  # brawlers count

        self.writeVint(self.player.gems)  # gems
        self.writeVint(0)
        self.writeVint(99)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(2)
        self.writeVint(1550832808)
