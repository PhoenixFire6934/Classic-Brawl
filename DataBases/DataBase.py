import json
import string
import random
from Utils.Helpers import Helpers

class DataBase:

    def loadAccount(self):
        with open('data.db', 'r') as read_data:
            for line in read_data.readlines():

                json_data = json.loads(line)
                dict = json.loads(json.dumps(json_data))  # loading and dumping json data from file

                if self.player.Token in dict:
                    self.player.name = dict[str(self.player.Token)]["name"]
                    self.player.gems = dict[str(self.player.Token)]["gems"]
                    self.player.gold = dict[str(self.player.Token)]["gold"]
                    self.player.tickets = dict[str(self.player.Token)]["tickets"]
                    self.player.brawlerID = dict[str(self.player.Token)]["brawlerID"]
                    self.player.skinID = dict[str(self.player.Token)]["skinID"]
                    self.player.trophies = dict[str(self.player.Token)]["trophies"]
                    self.player.profileIcon = dict[str(self.player.Token)]["profileIcon"]
                    self.player.brawlBoxes = dict[str(self.player.Token)]["brawlBoxes"]
                    self.player.bigBoxes = dict[str(self.player.Token)]["bigBoxes"]
                    self.player.shellySkin = dict[str(self.player.Token)]["shellySkin"]
                    self.player.nitaSkin = dict[str(self.player.Token)]["nitaSkin"]
                    self.player.coltSkin = dict[str(self.player.Token)]["coltSkin"]
                    self.player.bullSkin = dict[str(self.player.Token)]["bullSkin"]
                    self.player.jessieSkin = dict[str(self.player.Token)]["jessieSkin"]
                    self.player.brockSkin = dict[str(self.player.Token)]["brockSkin"]
                    self.player.dynamikeSkin = dict[str(self.player.Token)]["dynamikeSkin"]
                    self.player.boSkin = dict[str(self.player.Token)]["boSkin"]
                    self.player.elprimoSkin = dict[str(self.player.Token)]["elprimoSkin"]
                    self.player.barleySkin = dict[str(self.player.Token)]["barleySkin"]
                    self.player.pocoSkin = dict[str(self.player.Token)]["pocoSkin"]
                    self.player.ricoSkin = dict[str(self.player.Token)]["ricoSkin"]
                    self.player.darrylSkin = dict[str(self.player.Token)]["darrylSkin"]
                    self.player.pennySkin = dict[str(self.player.Token)]["pennySkin"]
                    self.player.piperSkin = dict[str(self.player.Token)]["piperSkin"]
                    self.player.pamSkin = dict[str(self.player.Token)]["pamSkin"]
                    self.player.frankSkin = dict[str(self.player.Token)]["frankSkin"]
                    self.player.mortisSkin = dict[str(self.player.Token)]["mortisSkin"]
                    self.player.taraSkin = dict[str(self.player.Token)]["taraSkin"]
                    self.player.spikeSkin = dict[str(self.player.Token)]["spikeSkin"]
                    self.player.crowSkin = dict[str(self.player.Token)]["crowSkin"]
                    self.player.geneSkin = dict[str(self.player.Token)]["geneSkin"]
                    self.player.tickSkin = dict[str(self.player.Token)]["tickSkin"]
                    self.player.leonSkin = dict[str(self.player.Token)]["leonSkin"]
                    self.player.rosaSkin = dict[str(self.player.Token)]["rosaSkin"]
                    self.player.carlSkin = dict[str(self.player.Token)]["carlSkin"]
                    self.player.bibiSkin = dict[str(self.player.Token)]["bibiSkin"]
                    self.player.bitSkin = dict[str(self.player.Token)]["8bitSkin"]
                    self.player.sandySkin = dict[str(self.player.Token)]["sandySkin"]
                    self.player.beaSkin = dict[str(self.player.Token)]["beaSkin"]
                    self.player.emzSkin = dict[str(self.player.Token)]["emzSkin"]
                    self.player.mrpSkin = dict[str(self.player.Token)]["mrpSkin"]
                    self.player.maxSkin = dict[str(self.player.Token)]["maxSkin"]
                    self.player.jackySkin = dict[str(self.player.Token)]["jackySkin"]
                    self.player.galeSkin = dict[str(self.player.Token)]["galeSkin"]
                    self.player.naniSkin = dict[str(self.player.Token)]["naniSkin"]
                    self.player.sproutSkin = dict[str(self.player.Token)]["sproutSkin"]
                    self.player.namecolor = dict[str(self.player.Token)]["namecolor"]
                    self.player.gadget = dict[str(self.player.Token)]["gadget"]
                    self.player.starpower = dict[str(self.player.Token)]["starpower"]
                    self.player.DoNotDistrub = dict[str(self.player.Token)]["DoNotDistrub"]
                    self.player.roomID = dict[str(self.player.Token)]["roomID"]

    def createAccount(self):
        data = {
            self.player.Token: {
                "lowID":self.player.LowID,
                "name": self.player.name,
                "gems": self.player.gems,
                "gold": self.player.gold,
                "tickets": self.player.tickets,
                "brawlerID": 0,
                "skinID": 0,
                "trophies": self.player.trophies,
                "profileIcon": 0,
                "namecolor":12,
                "brawlBoxes": self.player.brawlBoxes,
                "bigBoxes": self.player.bigBoxes,
                "shellySkin": 0,
                "nitaSkin": 0,
                "coltSkin": 0,
                "bullSkin": 0,
                "jessieSkin": 0,
                "brockSkin": 0,
                "dynamikeSkin": 0,
                "boSkin": 0,
                "elprimoSkin": 0,
                "barleySkin": 0,
                "pocoSkin": 0,
                "ricoSkin": 0,
                "darrylSkin": 0,
                "pennySkin": 0,
                "piperSkin": 0,
                "pamSkin": 0,
                "frankSkin": 0,
                "mortisSkin": 0,
                "taraSkin": 0,
                "spikeSkin": 0,
                "crowSkin": 0,
                "geneSkin":0,
                "tickSkin":0,
                "leonSkin":0,
                "rosaSkin":0,
                "carlSkin":0,
                "bibiSkin":0,
                "8bitSkin":0,
                "sandySkin":0,
                "beaSkin":0,
                "emzSkin":0,
                "mrpSkin":0,
                "maxSkin":0,
                "jackySkin":0,
                "galeSkin":0,
                "naniSkin":0,
                "sproutSkin":0,
                "gadget":255,
                "starpower":76,
                "DoNotDistrub":0,
                "roomID": 0
            }
        }

        with open('data.db', 'a+') as data_file:
            json.dump(data, data_file)  # writing data for new account
            data_file.write('\n')  # writing a new line



    def replaceValue(self, value_name, new_value):
        with open('data.db', 'r+') as file:
            list = []

            for line in file.readlines():
                json_data = json.loads(line)
                dict = json.loads(json.dumps(json_data))  # loading and dumping json data from file
                if self.player.Token in dict:
                    dict[str(self.player.Token)][str(value_name)] = new_value
                list.append(dict)
                file.close()

        with open('data.db', 'w') as o:
            for i in list:
                o.write(str(i).replace("'", '"') + '\n')
            o.close()




        # example usage: replaceValue(self, 'gems', 7777)



