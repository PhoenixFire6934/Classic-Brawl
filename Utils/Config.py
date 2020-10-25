import os
import json
import sys

class Config:
    def create_config():
        settings = {
            "Gems": 99999,
            "Gold": 99999,
            "Tickets": 99999,
            "Starpoints": 99999,
            "BrawlBox": 999,
            "BigBox": 9999
        }

        with open('config.json', 'w') as config_file:
            json.dump(settings, config_file)

