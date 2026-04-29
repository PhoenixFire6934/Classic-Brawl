from ByteStream.Writer import Writer

class BattleEndMessage(Writer):
    def __init__(self, client, player, gamemode: int, result: int, players: list, 
                 trophy_change: int = 0, new_trophies: int = 0,
                 tokens_gained: int = 0, exp_gained: int = 0):
        super().__init__(client)
        self.id = 23456
        self.player  = player
        self.gamemode    = gamemode
        self.result  = result
        self.players = players
        self.trophy_change = trophy_change
        self.new_trophies = new_trophies
        self.tokens_gained = tokens_gained
        self.exp_gained = exp_gained

    def encode(self):
        current_brawler = str(self.player.home_brawler)
        
        self.writeVInt(self.gamemode)
        self.writeVInt(self.result)
        self.writeVInt(self.tokens_gained)  # Tokens Gained
        self.writeVInt(self.trophy_change)  # Trophies Result
        self.writeVInt(0)  # Power Play Points Gained
        self.writeVInt(0)  # Doubled Tokens
        self.writeVInt(0)  # Double Token Event
        self.writeVInt(self.player.token_doubler)  # Token Doubler Remaining
        self.writeVInt(0)  # Big Game/Robo Rumble Time
        self.writeVInt(0)  # Epic Win Power Play Points
        self.writeVInt(0)  # Championship Level Passed
        self.writeVInt(0)  # Challenge Reward Type
        self.writeVInt(0)  # Challenge Reward Amount
        self.writeVInt(0)  # Championship Losses Left
        self.writeVInt(0)  # Championship Maximum Losses
        self.writeVInt(0)  # Coin Shower Event
        self.writeVInt(0)  # Underdog Trophies
        
        # Battle Result Type
        if self.gamemode == 2 or self.gamemode == 5:  # Showdown
            self.writeVInt(31)
        else:
            self.writeVInt(16)

        self.writeVInt(0)  # Championship Challenge Type
        self.writeVInt(0)  # Championship Cleared

        # Players Array
        self.writeVInt(len(self.players))
        for hero in self.players:
            team: int = 0
            if hero["isPlayer"] == 1 and hero["team"] == 1: 
                team += 1
            if hero["team"] != self.players[0]["team"]: 
                team += 2
            
            self.writeVInt(team)
            self.writeDataReference(*hero["id"])
            self.writeDataReference(*hero["skin"])
            
            if hero["isPlayer"] == 1:
                self.writeVInt(self.new_trophies)  # Player trophies
            else:
                self.writeVInt(0)  # Bot trophies
            
            self.writeVInt(0)  # Power Play Points
            self.writeVInt(1)  # Brawler Power Level
            self.writeBoolean(hero["isPlayer"] == 1)
            
            if hero["isPlayer"] == 1:
                self.writeLong(self.player.ID)
            
            self.writeString(hero["name"])
            self.writeVInt(self.player.exp_points // 100)  # Experience Level
            self.writeVInt(28000000)  # Profile Icon
            self.writeVInt(43000000)  # Name Color

        # Experience Array
        if self.gamemode in [2, 5]:  # Showdown
            self.writeVInt(1)
            self.writeVInt(0)  # Normal Experience ID
            self.writeVInt(self.exp_gained)  # Normal Experience Gained
        else:  # 3v3
            self.writeVInt(1)  # Was 0, became 1
            self.writeVInt(0)  # Normal Experience ID
            self.writeVInt(self.exp_gained)  # Normal Experience Gained

        # Rank Up and Level Up Bonus Array
        self.writeVInt(0)

        # Trophies and Experience Bars
        self.writeVInt(1)
        self.writeVInt(1)  # Trophies Bar Milestone ID
        self.writeVInt(self.new_trophies)  # Brawler Trophies
        self.writeVInt(self.player.brawlers_high_trophies.get(current_brawler, 0))  # Brawler Trophies for Rank
        self.writeVInt(5)  # Experience Bar Milestone ID
        self.writeVInt(self.player.exp_points)  # Player Experience
        self.writeVInt(self.player.exp_points)  # Player Experience for Level

        self.writeDataReference(28, self.player.profile_icon)
        self.writeBoolean(False)  # Play Again Entry