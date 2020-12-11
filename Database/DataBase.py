import json
import string
import random
from tinydb import TinyDB, Query
from Utils.Helpers import Helpers

class DataBase:



    def loadAccount(self):
        db = TinyDB('data.db')
        query = Query()
        user_data = db.search(query.token == str(self.player.token))
        if user_data:
            self.player.name = user_data[0]["info"]["name"]
            self.player.gems = user_data[0]["info"]["gems"]
            self.player.gold = user_data[0]["info"]["gold"]
            self.player.starPoints = user_data[0]["info"]["starpoints"]
            self.player.tickets = user_data[0]["info"]["tickets"]
            self.player.brawler_id = user_data[0]["info"]["brawlerID"]
            self.player.skin_id = user_data[0]["info"]["skinID"]
            self.player.trophies = user_data[0]["info"]["trophies"]
            self.player.profileIcon = user_data[0]["info"]["profileIcon"]
            self.player.brawlBoxes = user_data[0]["info"]["brawlBoxes"]
            self.player.bigBoxes = user_data[0]["info"]["bigBoxes"]
            self.player.shellySkin = user_data[0]["info"]["shellySkin"]
            self.player.nitaSkin = user_data[0]["info"]["nitaSkin"]
            self.player.coltSkin = user_data[0]["info"]["coltSkin"]
            self.player.bullSkin = user_data[0]["info"]["bullSkin"]
            self.player.jessieSkin = user_data[0]["info"]["jessieSkin"]
            self.player.brockSkin = user_data[0]["info"]["brockSkin"]
            self.player.dynamikeSkin = user_data[0]["info"]["dynamikeSkin"]
            self.player.boSkin = user_data[0]["info"]["boSkin"]
            self.player.elprimoSkin = user_data[0]["info"]["elprimoSkin"]
            self.player.barleySkin = user_data[0]["info"]["barleySkin"]
            self.player.pocoSkin = user_data[0]["info"]["pocoSkin"]
            self.player.ricoSkin = user_data[0]["info"]["ricoSkin"]
            self.player.darrylSkin = user_data[0]["info"]["darrylSkin"]
            self.player.pennySkin = user_data[0]["info"]["pennySkin"]
            self.player.piperSkin = user_data[0]["info"]["piperSkin"]
            self.player.pamSkin = user_data[0]["info"]["pamSkin"]
            self.player.frankSkin = user_data[0]["info"]["frankSkin"]
            self.player.mortisSkin = user_data[0]["info"]["mortisSkin"]
            self.player.taraSkin = user_data[0]["info"]["taraSkin"]
            self.player.spikeSkin = user_data[0]["info"]["spikeSkin"]
            self.player.crowSkin = user_data[0]["info"]["crowSkin"]
            self.player.geneSkin = user_data[0]["info"]["geneSkin"]
            self.player.tickSkin = user_data[0]["info"]["tickSkin"]
            self.player.leonSkin = user_data[0]["info"]["leonSkin"]
            self.player.rosaSkin = user_data[0]["info"]["rosaSkin"]
            self.player.carlSkin = user_data[0]["info"]["carlSkin"]
            self.player.bibiSkin = user_data[0]["info"]["bibiSkin"]
            self.player.bitSkin = user_data[0]["info"]["8bitSkin"]
            self.player.sandySkin = user_data[0]["info"]["sandySkin"]
            self.player.beaSkin = user_data[0]["info"]["beaSkin"]
            self.player.emzSkin = user_data[0]["info"]["emzSkin"]
            self.player.mrpSkin = user_data[0]["info"]["mrpSkin"]
            self.player.maxSkin = user_data[0]["info"]["maxSkin"]
            self.player.jackySkin = user_data[0]["info"]["jackySkin"]
            self.player.galeSkin = user_data[0]["info"]["galeSkin"]
            self.player.naniSkin = user_data[0]["info"]["naniSkin"]
            self.player.sproutSkin = user_data[0]["info"]["sproutSkin"]
            self.player.namecolor = user_data[0]["info"]["namecolor"]
            self.player.gadget = user_data[0]["info"]["gadget"]
            self.player.starpower = user_data[0]["info"]["starpower"]
            self.player.DoNotDistrubMessage = user_data[0]["info"]["DoNotDistrub"]
            self.player.room_id = user_data[0]["info"]["roomID"]
            self.player.brawlers_trophies = user_data[0]["info"]["brawlersTrophies"]




    def createAccount(self):

        db = TinyDB('data.db')

        data = {
            "token": str(self.player.token),

            "info":
                {
                    "name": self.player.name,
                    "lowID": self.player.low_id,
                    "gems": self.player.gems,
                    "gold": self.player.gold,
                    "starpoints": self.player.starPoints,
                    "tickets": self.player.tickets,
                    "brawlerID": 0,
                    "skinID": 0,
                    "trophies": self.player.trophies,
                    "profileIcon": 0,
                    "namecolor": 12,
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
                    "geneSkin": 0,
                    "tickSkin": 0,
                    "leonSkin": 0,
                    "rosaSkin": 0,
                    "carlSkin": 0,
                    "bibiSkin": 0,
                    "8bitSkin": 0,
                    "sandySkin": 0,
                    "beaSkin": 0,
                    "emzSkin": 0,
                    "mrpSkin": 0,
                    "maxSkin": 0,
                    "jackySkin": 0,
                    "galeSkin": 0,
                    "naniSkin": 0,
                    "sproutSkin": 0,
                    "gadget": 255,
                    "starpower": 76,
                    "DoNotDistrub": 0,
                    "roomID": 0,
                    "brawlersTrophies": self.player.brawlers_trophies

                }

        }

        db.insert(data)


    def getAllPlayers(self):
        db = TinyDB('data.db')
        query = Query()
        name_list =[]

        for i in db.all():
            token = i['token']
            name = db.search(query.token == str(token))[0]['info']
            name_list.append(name)

        return name_list


    def replaceValue(self, value_name, new_value):
        db = TinyDB('data.db')
        query = Query()
        data = db.search(query.token == str(self.player.token))
        user_data = data[0]
        user_data["info"][str(value_name)] = new_value
        db.update(user_data, query.token == str(self.player.token))









