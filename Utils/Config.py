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
          "BrawlBoxTokens": 9900,
          "BigBoxTokens": 9990,
          "Trophies": 0,
          "ExperiencePoints": 99999,
          "BrawlerTrophies": 0,
          "BrawlerTrophiesForRank": 0,
          "BrawlerPowerLevel": 8,
          "BrawlerUpgradePoints": 0,
          "ThemeID": 0,
          "SupportedContentCreator": "",
          "ShowPacketsInLog": False,
          "Maintenance": False,
          "MaintenanceTime": 3600,
          "Patch": False,
          "PatchUrl": "http://192.168.0.103:8080/",
          "UpdateUrl": "https://github.com/PhoenixFire6879/Classic-Brawl"
}


        with open('config.json', 'w') as config_file:
            json.dump(settings, config_file)

    def GetValue():
      config_settings = {}

      Config_file = open('config.json', 'r')
      config_values = Config_file.read()

      config_settings = json.loads(config_values)
      return config_settings

