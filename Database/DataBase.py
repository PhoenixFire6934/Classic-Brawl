from tinydb import TinyDB, Query

class DataBase:


    def loadAccount(self):
        db = TinyDB('data.db')
        query = Query()
        user_data = db.search(query.token == str(self.player.token))
        if user_data:
            self.player.name = user_data[0]["info"]["name"]
            self.player.gems = user_data[0]["info"]["gems"]
            self.player.gold = user_data[0]["info"]["gold"]
            self.player.star_points = user_data[0]["info"]["starpoints"]
            self.player.tickets = user_data[0]["info"]["tickets"]
            self.player.brawler_id = user_data[0]["info"]["brawlerID"]
            self.player.skin_id = user_data[0]["info"]["skinID"]
            self.player.trophies = user_data[0]["info"]["trophies"]
            self.player.profile_icon = user_data[0]["info"]["profileIcon"]
            self.player.brawl_boxes = user_data[0]["info"]["brawlBoxes"]
            self.player.big_boxes = user_data[0]["info"]["bigBoxes"]
            self.player.brawlers_skins = user_data[0]["info"]["brawlersSkins"]
            self.player.name_color = user_data[0]["info"]["namecolor"]
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
                    "starpoints": self.player.star_points,
                    "tickets": self.player.tickets,
                    "brawlerID": 0,
                    "skinID": 0,
                    "trophies": self.player.trophies,
                    "profileIcon": 0,
                    "namecolor": self.player.name_color,
                    "brawlBoxes": self.player.brawl_boxes,
                    "bigBoxes": self.player.big_boxes,
                    "gadget": 255,
                    "starpower": 76,
                    "DoNotDistrub": 0,
                    "roomID": 0,
                    "brawlersSkins": self.player.brawlers_skins,
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









