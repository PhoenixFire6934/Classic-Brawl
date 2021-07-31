class LogicPlayerStats:

    def getPlayerStats(self, accountData):

        playerStats = {

            '3v3Victories': 0,
            'ExperiencePoints': accountData['ExperiencePoints'],
            'Trophies': accountData['Trophies'],
            'HighestTrophies': accountData['HighestTrophies'],
            'UnlockedBrawlersCount': len(accountData['UnlockedBrawlers']),
            'Unknown2': 0,
            'ProfileIconID': 28000000 + accountData['ProfileIcon'],
            'SoloVictories': 0,
            'BestRoboRumbleTime': 9999,
            'BestTimeAsBigBrawler': 99999,
            'DuoVictories': 0,
            'HighestBossFightLvlPassed': 21,
            'Unknown4': 0,
            'PowerPlayRank': 1,
            'MostChallengeWins': 0

        }

        return playerStats