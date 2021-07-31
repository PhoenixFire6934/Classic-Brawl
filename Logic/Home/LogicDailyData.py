from datetime import datetime
from Logic.Home.LogicShopData import LogicShopData

class LogicDailyData:

    def encode(self):

        time_stamp = int(datetime.timestamp(datetime.now()))

        self.writeVInt(time_stamp)
        self.writeVInt(time_stamp)

        self.writeVInt(self.player.trophies)
        self.writeVInt(self.player.high_trophies)
        self.writeVInt(self.player.high_trophies)

        self.writeVInt(self.player.trophy_reward)
        self.writeVInt(self.player.exp_points)

        self.writeDataReference(28, self.player.profile_icon)
        self.writeDataReference(43, self.player.name_color)

        self.writeVInt(50)
        for x in range(50):
            self.writeVInt(x)

        self.writeVInt(len(self.player.selected_skins))
        for x in self.player.selected_skins:
            self.writeDataReference(29, self.player.selected_skins[x])

        self.writeVInt(len(self.player.unlocked_skins))
        for x in self.player.unlocked_skins:
            self.writeDataReference(29, x)

        self.writeVInt(0)  # Unknown Array
        for x in range(0):
            self.writeDataReference(0,0)

        self.writeVInt(0)      # Leaderboard Global TID
        self.writeVInt(50000)  # Trophy Road Reached Icon
        self.writeVInt(0)      # Unknown

        self.writeUInt8(0)
        self.writeVInt(0)
        self.writeUInt8(0)

        self.writeVInt(self.player.token_doubler)
        self.writeVInt(99999)  # Trophy Road Timer
        self.writeVInt(0)      # Power Play Timer
        self.writeVInt(99999)  # Brawl Pass Timer

        self.writeVInt(0)  # Unknown

        self.writeBoolean(False)
        self.writeBoolean(False)

        self.writeUInt8(8) # Shop Token Doubler

        self.writeVInt(2) # Unknown
        self.writeVInt(2) # Unknown
        self.writeVInt(2) # Unknown

        self.writeVInt(0) # Name Change Cost
        self.writeVInt(0) # Name Change Timer


        LogicShopData.encodeShopOffers(self)

        self.writeVInt(0)  # AdStatus
        for x in range(0):
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)

        self.writeVInt(200) # Available Battle Tokens
        self.writeVInt(0)   # Time till Bonus Tokens

        self.writeVInt(0)  # Unknown Array
        for x in range(0):
            self.writeVInt(x)

        self.writeVInt(self.player.tickets)
        self.writeVInt(0)  # Unknown

        self.writeDataReference(16, self.player.home_brawler)

        self.writeString(self.player.region)
        self.writeString(self.player.content_creator)

        self.writeVInt(0)  # Unknown Array
        for x in range(0):
            self.writeInt(0)
            self.writeInt(0)

        self.writeVInt(0)  # CooldownEntry
        for x in range(0):
            self.writeVInt(0)
            self.writeDataReference(0, 0)
            self.writeVInt(0)

        self.writeVInt(0)  # BrawlPassSeasonData
        for x in range(0):
            pass

        self.writeVInt(0)  # ProLeagueSeasonData
        for x in range(0):
            self.writeVInt(0)
            self.writeVInt(0)

        self.writeBoolean(True) # LogicQuests
        if True:
            self.writeVInt(0)
            for x in range(0):
                pass




