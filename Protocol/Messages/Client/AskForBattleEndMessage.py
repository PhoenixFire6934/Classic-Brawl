from ByteStream.Reader import Reader
from Protocol.Messages.Server.BattleEndMessage import BattleEndMessage
from Protocol.Messages.Server.OwnHomeDataMessage import OwnHomeDataMessage

class AskForBattleEndMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client
        self.players: list = []

    def decode(self):
        self.result   = self.readVInt()
        self.unk      = self.readVInt()
        self.rank     = self.readVInt()
        self.mapID    = self.readDataReference()

        self.count    = self.readVInt()

        for player in range(self.count):
            self.players.append({
                'id': self.readDataReference(), 
                'skin': self.readDataReference(), 
                'team': self.readVInt(), 
                'isPlayer': self.readVInt(), 
                'name': self.readString()
            })

    def process(self, db):
        if self.player.status != 8: 
            return
        if self.count not in [3, 6, 10]: 
            return

        # We determine the type of battle
        if self.count == 10:  # Solo Showdown
            self.type = 2
            is_showdown = True
        elif self.count == 6 and self.rank != 0:  # Duo Showdown
            self.type = 5
            is_showdown = True
        else:  # 3v3
            is_showdown = False
            if self.rank != 0:
                if len(self.players) >= 2 and self.players[0]['team'] == self.players[1]['team']:
                    self.type = 5
                else:
                    self.type = 2
            else:
                self.type = 0

        # Get the player's current brawler
        current_brawler = str(self.player.home_brawler)
        current_trophies = self.player.brawlers_trophies.get(current_brawler, 0)
    
        # Calculating the change in trophies
        trophy_change = self.calculate_trophy_change(
            current_trophies, 
            self.rank, 
            is_showdown
        )
    
        # Applying trophy changes
        new_trophies = max(0, current_trophies + trophy_change)
        self.player.brawlers_trophies[current_brawler] = new_trophies
    
        # Update the brawler's record if necessary
        if new_trophies > self.player.brawlers_high_trophies.get(current_brawler, 0):
            self.player.brawlers_high_trophies[current_brawler] = new_trophies
    
        # Updating the total number of trophies
        total_trophies = sum(self.player.brawlers_trophies.values())
        self.player.trophies = total_trophies
        
        # Updating the player's overall record
        if total_trophies > self.player.high_trophies:
            self.player.high_trophies = total_trophies
            db.update_player_account(self.player.token, 'HighestTrophies', self.player.high_trophies)
    
        # Token calculation
        tokens_gained = self.calculate_tokens(is_showdown, self.rank)
        self.player.resources[0]['Amount'] += tokens_gained
    
        # Calculation of experience
        exp_gained = self.calculate_experience(is_showdown, self.rank)
        self.player.exp_points += exp_gained
    
        # Save in the database
        db.update_player_account(self.player.token, 'BrawlersTrophies', self.player.brawlers_trophies)
        db.update_player_account(self.player.token, 'BrawlersHighestTrophies', self.player.brawlers_high_trophies)
        db.update_player_account(self.player.token, 'Trophies', self.player.trophies)
        db.update_player_account(self.player.token, 'Resources', self.player.resources)
        db.update_player_account(self.player.token, 'ExperiencePoints', self.player.exp_points)
    
        # We send the results (the same for both modes)
        BattleEndMessage(
            self.client, self.player, self.type, self.result, 
            self.players, trophy_change, new_trophies,
            tokens_gained, exp_gained
        ).send()
        OwnHomeDataMessage(self.client, self.player).send()

    def calculate_trophy_change(self, current_trophies, rank, is_showdown):
        """Calculates the change in trophies based on the current trophies and the result"""
        if current_trophies < 50:
            win_trophies = 8
            lose_trophies = 0
        elif current_trophies < 100:
            win_trophies = 7
            lose_trophies = -2
        elif current_trophies < 200:
            win_trophies = 6
            lose_trophies = -3
        elif current_trophies < 300:
            win_trophies = 5
            lose_trophies = -4
        elif current_trophies < 400:
            win_trophies = 4
            lose_trophies = -5
        elif current_trophies < 500:
            win_trophies = 3
            lose_trophies = -6
        elif current_trophies < 600:
            win_trophies = 2
            lose_trophies = -7
        else:
            win_trophies = 1
            lose_trophies = -8
        
        if is_showdown:
            if rank == 1:
                return win_trophies + 2
            elif rank <= 3:
                return win_trophies
            elif rank <= 5:
                return lose_trophies // 2
            else:
                return lose_trophies
        else:
            if rank == 0:
                return win_trophies
            else:
                return lose_trophies

    def calculate_tokens(self, is_showdown, rank):
        """Calculates the number of tokens per battle"""
        if is_showdown:
            if rank == 1:
                return 30
            elif rank <= 3:
                return 20
            elif rank <= 5:
                return 10
            else:
                return 5
        else:
            if rank == 0:
                return 20
            else:
                return 10

    def calculate_experience(self, is_showdown, rank):
        """Calculates experience per battle"""
        if is_showdown:
            if rank == 1:
                return 100
            elif rank <= 3:
                return 75
            elif rank <= 5:
                return 50
            else:
                return 25
        else:
            if rank == 0:
                return 80
            else:
                return 40