import random

class Boxes:


    boxes = [
        {
            'Name': 'Brawl Box',
            'MinCoins': 13,
            'MaxCoins': 120,
            'MinUpgradePoints': 4,
            'MaxUpgradePoints': 50,
            'MinTickets': 1,
            'MaxTickets': 10,
            'Gems': [3, 5, 6, 8, 12, 14, 18, 20],
            'TokensDoubler': 0
        },

        {
            'Name': 'Big Box',
            'MinCoins': 43,
            'MaxCoins': 500,
            'MinUpgradePoints': 20,
            'MaxUpgradePoints': 150,
            'MinTickets': 1,
            'MaxTickets': 10,
            'Gems': [3, 5, 6, 8, 12, 14, 18, 20],
            'TokensDoubler': [200, 400, 600]
        },

        {
            'Name': 'Shop Big Box',
            'Price': 30,
            'MinCoins': 43,
            'MaxCoins': 500,
            'MinUpgradePoints': 20,
            'MaxUpgradePoints': 150,
            'MinTickets': 1,
            'MaxTickets': 10,
            'Gems': [3, 5, 6, 8, 12, 14, 18, 20],
            'TokensDoubler': [200, 400, 600]
        },

        {
            'Name': 'Mega Box',
            'Price': 80,
            'MinCoins': 150,
            'MaxCoins': 1200,
            'MinUpgradePoints': 25,
            'MaxUpgradePoints': 200,
            'MinTickets': 1,
            'MaxTickets': 16,
            'Gems': [3, 5, 6, 8, 12, 14, 18, 20, 24, 28],
            'TokensDoubler': [200, 400, 600]
        }
    ]

    reward_id = [
        {
            'Name': 'Brawler',
            'ID': 1,
        },

        {
            'Name': 'TokensDoubler',
            'ID': 2,
        },

        {
            'Name': 'Tickets',
            'ID': 3,
        },

        {
            'Name': 'Unknown',
            'ID': 4,
        },

        {
            'Name': 'Unknown',
            'ID': 5,
        },

        {
            'Name': 'UpgradePoints',
            'ID': 6,
        },

        {
            'Name': 'Golds',
            'ID': 7,
        },

        {
            'Name': 'Gems',
            'ID': 8,
        }
    ]