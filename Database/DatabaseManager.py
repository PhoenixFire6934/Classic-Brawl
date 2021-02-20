from Logic.Player import Players
import json
from tinydb import TinyDB, Query, database

class DataBase:


    def loadAccount(self):
        db = TinyDB('Database/Player/data.db')
        query = Query()
        user_data = db.search(query.token == str(self.player.token))
        if user_data:
            self.player.name = user_data[0]["info"]["name"]
            self.player.low_id = user_data[0]["info"]["lowID"]
            self.player.IsFacebookLinked = user_data[0]["info"]["isFBLinked"]
            self.player.FacebookID = user_data[0]["info"]["facebookID"]
            self.player.club_low_id = user_data[0]["info"]["clubID"]
            self.player.club_role = user_data[0]["info"]["clubRole"]
            self.player.player_experience = user_data[0]["info"]["playerExp"]
            self.player.solo_wins = user_data[0]["info"]["soloWins"]
            self.player.duo_wins = user_data[0]["info"]["duoWins"]
            self.player.ThreeVSThree_wins = user_data[0]["info"]["3vs3Wins"]
            self.player.gems = user_data[0]["info"]["gems"]
            self.player.gold = user_data[0]["info"]["gold"]
            self.player.star_points = user_data[0]["info"]["starpoints"]
            self.player.tickets = user_data[0]["info"]["tickets"]
            self.player.tokensdoubler = user_data[0]["info"]["tokensdoubler"]
            self.player.player_tokens = user_data[0]["info"]["playerTokens"]
            self.player.brawler_id = user_data[0]["info"]["brawlerID"]
            self.player.skin_id = user_data[0]["info"]["skinID"]
            self.player.profile_icon = user_data[0]["info"]["profileIcon"]
            self.player.brawl_boxes = user_data[0]["info"]["brawlBoxes"]
            self.player.big_boxes = user_data[0]["info"]["bigBoxes"]
            self.player.brawlers_skins = user_data[0]["info"]["brawlersSkins"]
            self.player.name_color = user_data[0]["info"]["namecolor"]
            self.player.starpower = user_data[0]["info"]["starpower"]
            self.player.DoNotDistrubMessage = user_data[0]["info"]["DoNotDistrub"]
            self.player.room_id = user_data[0]["info"]["roomID"]
            self.player.brawlers_trophies_in_rank = user_data[0]["info"]["brawlersTrophiesForRank"]
            self.player.brawlers_upgradium = user_data[0]["info"]["brawlersUpgradePoints"]
            self.player.Brawler_level = user_data[0]["info"]["brawlerPowerLevel"]
            self.player.brawlers_trophies = user_data[0]["info"]["brawlersTrophies"]

            if self.player.UnlockType == "Off":
                self.player.BrawlersUnlockedState = user_data[0]["info"]["UnlockedBrawlers"]

            player_total_trophies = 0
            for BrawlerID in self.player.brawlers_trophies.keys():
                player_total_trophies += self.player.brawlers_trophies[BrawlerID]
            self.player.trophies = player_total_trophies
            DataBase.replaceValue(self, 'trophies', self.player.trophies)

            if self.player.trophies < user_data[0]["info"]["highesttrophies"]:
                self.player.highest_trophies = user_data[0]["info"]["highesttrophies"]
            else:
                self.player.highest_trophies = self.player.trophies
                
            DataBase.replaceValue(self, 'highesttrophies', self.player.highest_trophies)

    def createAccount(self):
        Players.CreateNewBrawlersList()
        db = TinyDB('Database/Player/data.db')

        data = {
            "token": str(self.player.token),

            "info":
                {
                    "name": self.player.name,
                    "lowID": self.player.low_id,
                    "clubID": 0,
                    "clubRole": 0,
                    "isFBLinked": 0,
                    "facebookID": self.player.FacebookID,
                    "playerExp": self.player.player_experience,
                    "soloWins": self.player.solo_wins,
                    "duoWins": self.player.duo_wins,
                    "3vs3Wins": self.player.ThreeVSThree_wins,
                    "gems": self.player.gems,
                    "gold": self.player.gold,
                    "starpoints": self.player.star_points,
                    "tokensdoubler": self.player.tokensdoubler,
                    "playerTokens": self.player.player_tokens,
                    "tickets": self.player.tickets,
                    "brawlerID": 0,
                    "skinID": 0,
                    "trophies": self.player.trophies,
                    "highesttrophies": self.player.trophies,
                    "profileIcon": 0,
                    "namecolor": self.player.name_color,
                    "brawlBoxes": self.player.brawl_boxes,
                    "bigBoxes": self.player.big_boxes,
                    "starpower": 76,
                    "DoNotDistrub": 0,
                    "roomID": 0,
                    "brawlersSkins": self.player.brawlers_skins,
                    "brawlersTrophies": self.player.brawlers_trophies,
                    "brawlersTrophiesForRank": self.player.brawlers_trophies_in_rank,
                    "brawlersUpgradePoints": self.player.brawlers_upgradium,
                    "brawlerPowerLevel": self.player.Brawler_level,
                    "UnlockedBrawlers": self.player.BrawlersUnlockedState
                }
        }

        db.insert(data)

    def getAllPlayers(self):
        db = TinyDB('Database/Player/data.db')
        query = Query()
        name_list =[]

        for i in db.all():
            token = i['token']
            name = db.search(query.token == str(token))[0]['info']
            name_list.append(name)

        return name_list

    def getSpecifiedValue(self, value_name):
        db = TinyDB('Database/Player/data.db')
        query = Query()
        name_list =[]

        self.requested_val = db.search(query.token == str(self.player.token))[0]['info'][value_name]


    def replaceValue(self, value_name, new_value):
        db = TinyDB('Database/Player/data.db')
        query = Query()
        data = db.search(query.token == str(self.player.token))
        user_data = data[0]
        user_data["info"][str(value_name)] = new_value
        db.update(user_data, query.token == str(self.player.token))


    # Gameroom
    def createGameroomDB(self):
        db = TinyDB('Database/Gameroom/gameroom.db')
        data = { 
            "room_id": self.player.room_id,
            "info": {
                "roomType": self.roomType,
                "mapID": self.player.map_id,
                "PlayerCount": 1,
                self.player.low_id: {
                    "host": 1,
                    "lowID": self.player.low_id,
                    "name": self.player.name,
                    "Team": self.player.team,
                    "Ready": self.player.isReady,
                    "brawlerID": self.player.brawler_id,
                    "starpower": self.player.starpower,
                    "profileIcon": self.player.profile_icon,
                    "namecolor": self.player.name_color
                }
            }
        }
        db.insert(data)

    def loadGameroom(self):
        db = TinyDB('Database/Gameroom/gameroom.db')
        query = Query()
        gameroom_data = db.search(query.room_id == self.player.room_id)

        self.playersdata = {}
        if gameroom_data:
            self.roomType = gameroom_data[0]["info"]["roomType"]
            self.mapID = gameroom_data[0]["info"]["mapID"]
            self.playerCount = gameroom_data[0]["info"]["PlayerCount"]
            for Players,info in gameroom_data[0]["info"].items():
                if Players != "PlayerCount" and Players != "mapID" and Players != "roomType":
                    self.playersdata[Players] = {}
                    self.playersdata[Players]["IsHost"] = info["host"]
                    self.playersdata[Players]["name"] = info["name"]
                    self.playersdata[Players]["Team"] = info["Team"]
                    self.playersdata[Players]["Ready"] = info["Ready"]
                    self.playersdata[Players]["LowID"] = Players
                    self.playersdata[Players]["profileIcon"] = info["profileIcon"]
                    self.playersdata[Players]["namecolor"] = info["namecolor"]
                    self.playersdata[Players]["brawlerID"] = info["brawlerID"]
                    self.playersdata[Players]["starpower"] = info["starpower"]
        else:
            playerdb = TinyDB('Database/Player/data.db')
            query = Query()
            data = playerdb.search(query.token == str(self.player.token))
            user_data = data[0]
            user_data["info"]["roomID"] = 0
            self.player.room_id = 0
            playerdb.update(user_data, query.token == str(self.player.token))

    def replaceGameroomValue(self, value_name, new_value, type):
        db = TinyDB('Database/Gameroom/gameroom.db')
        query = Query()
        valueToRemove = Query()
        data = db.search(query.room_id == self.player.room_id)
        gameroom_data = data[0]

        if type == "room":
            gameroom_data["info"][str(value_name)] = new_value
            db.update(gameroom_data, query.room_id == self.player.room_id)
        elif type == "player":
            gameroom_data["info"][str(value_name)] = new_value
            db.update(gameroom_data, query.room_id == self.player.room_id)
        elif type == "removePlayer":
            if gameroom_data["info"][str(new_value)]["host"] == 1:
                db.remove(query.room_id == self.player.room_id)
            else:
                db.remove(query.room_id.any(valueToRemove == str(new_value)))
        else:
            db.remove(query.room_id == self.player.room_id)
    
    def UpdateGameroomPlayerInfo(self, low_id):
        db = TinyDB('Database/Gameroom/gameroom.db')
        query = Query()
        player = Query()
        data = db.search(query.room_id == self.player.room_id)
        gameroom_data = data[0]

        gameroom_data["info"][str(low_id)]["Team"] = self.player.team
        gameroom_data["info"][str(low_id)]["Ready"] = self.player.isReady
        gameroom_data["info"][str(low_id)]["brawlerID"] = self.player.brawler_id
        gameroom_data["info"][str(low_id)]["starpower"] = self.player.starpower
        gameroom_data["info"][str(low_id)]["profileIcon"] = self.player.profile_icon
        gameroom_data["info"][str(low_id)]["namecolor"] = self.player.name_color

        db.update(gameroom_data, query.room_id == self.player.room_id)


    def createClub(self, clubid):
        clubdb = TinyDB('Database/Club/club.db')
        chatdb = TinyDB('Database/Club/chat.db')

        data = {
            "clubID": clubid,
            "info": {
                "clubID": clubid,
                "name": self.clubName,                          
                "description": self.clubdescription,
                "region": "RO",
                "badgeID": self.clubbadgeID,
                "type": self.clubtype,
                "trophiesneeded": self.clubtrophiesneeded,
                "trophies": self.player.trophies,
                "members": {
                    "totalmembers": 1,
                    str(self.player.low_id): self.player.name
                }
            }
        }
        clubdb.insert(data)
        msgData = {
            "clubID": clubid,
            "info": {
                "Total": 1,
                "1": {
                    "Event": 2,
                    "Tick": 1,
                    "PlayerID": self.player.low_id,
                    "PlayerName": self.player.name,
                    "PlayerRole": 2,
                    "Message": "Welcome to your new club!"
                }
            }
        }
        chatdb.insert(msgData)

    def CountClub(self, minMembers, maxMembers, clubType, maxListLength):
        db = TinyDB('Database/Club/club.db')
        query = Query()
        self.club_list = []
        self.club_data = []

        self.AllianceCount = 0
        for club in db.all():
            if self.AllianceCount != maxListLength:
                club_id = club['clubID']
                clubInfo = db.search(query.clubID == club_id)[0]['info']
                if clubInfo['members']['totalmembers'] >= minMembers and clubInfo['members']['totalmembers'] < maxMembers and clubInfo['type'] <= clubType:
                    self.club_list.append(club_id)
                    self.club_data.append(clubInfo)
                    self.AllianceCount += 1
            else:
                break
            #if info["members"]["totalmembers"] >= minMembers and info["members"]["totalmembers"] < maxMembers and info["type"] <= clubType and self.AllianceCount <= maxListLength:
            
    
    def loadClub(self, clubid):
        db = TinyDB('Database/Club/club.db')
        query = Query()
        data = db.search(query.clubID == clubid)
        club_data = data[0]
        self.plrids = []
        self.clubName = club_data["info"]["name"]
        self.clubdescription = club_data["info"]["description"]
        self.clubregion = club_data["info"]["region"]
        self.clubbadgeID = club_data["info"]["badgeID"]
        self.clubtype = club_data["info"]["type"]
        self.clubtrophiesneeded = club_data["info"]["trophiesneeded"]
        self.clubtrophies = club_data["info"]["trophies"]
        self.clubmembercount = club_data["info"]["members"]["totalmembers"]
        for plridentifier, data in club_data["info"]["members"].items():
            if plridentifier != "totalmembers":
                self.plrids.append(int(plridentifier))

    def AddMember(self, AllianceID, PlayerID, PlayerName, Action):
        db = TinyDB('Database/Club/club.db')
        chatdb = TinyDB('Database/Club/chat.db')
        query = Query()
        data = db.search(query.clubID == self.player.club_low_id)
        data = data[0]

        if Action == 0:
            db.remove(query.clubID == self.player.club_low_id)

            chatdb.remove(query.clubID == self.player.club_low_id)

        elif Action == 1:
            data['info']['members']['totalmembers'] += 1
            data['info']['members'][str(PlayerID)] = PlayerName

            db.update(data, query.clubID == self.player.club_low_id)

        elif Action == 2:
            try:
                data['info']['members']['totalmembers'] -= 1
                data['info']['members'].pop(str(PlayerID))

                db.update(data, query.clubID == self.player.club_low_id)
            except:
                pass

    def GetMemberData(self, Low_id):
        db = TinyDB('Database/Player/data.db')
        query = Query()
        try:
            self.players = DataBase.getAllPlayers(self)
            print(self.players[0])
            for i in range(len(self.players)):
                if self.players[i]['lowID'] == int(Low_id):
                    print(self.players[i])
                    self.lowplrid = self.players[i]['lowID']
                    self.plrrole = self.players[i]["clubRole"]
                    self.plrtrophies = self.players[i]["trophies"]
                    self.plrname = self.players[i]["name"]
                    self.plricon = self.players[i]["profileIcon"]
                    self.plrnamecolor = self.players[i]["namecolor"]
                    break


        except Exception as e:
            print(e)
            self.lowplrid = 1
            self.plrrole = 2
            self.plrtrophies = 0
            self.plrname = "Bot"
            self.plricon = 1
            self.plrnamecolor = 2

    def replaceClubValue(self, target, inf1, inf2, inf3, inf4, inf5):
        db = TinyDB('Database/Club/club.db')
        query = Query()
        data = db.search(query.clubID == self.player.club_low_id)
        club_data = data[0]

        club_data["info"]['description'] = inf1
        club_data["info"]['badgeID'] = inf2
        club_data["info"]['type'] = inf3
        club_data["info"]['trophiesneeded'] = inf4

        db.update(club_data, query.clubID == self.player.club_low_id)

    def GetmsgCount(self, clubID):
        db = TinyDB('Database/Club/chat.db')
        query = Query()
        data = db.search(query.clubID == self.player.club_low_id)
        data = data[0]
        self.MessageCount = data['info']['Total']

    def Addmsg(self, clubID, event, tick, Low_id, name, role, msg):
        db = TinyDB('Database/Club/chat.db')
        query = Query()
        data = db.search(query.clubID == self.player.club_low_id)
        data = data[0]
        index = 0
        for i in range(1, data['info']['Total'] + 1):
            index += 1
            if index == data['info']['Total']:
                data['info'][str(i + 1)] = {"Event": event, "Tick":  data['info'][str(i)]['Tick'] + 1, "PlayerID": Low_id, "PlayerName": name, "PlayerRole": role, "Message": msg}
                data['info']['Total'] = i + 1
                self.player.message_tick = data['info'][str(i + 1)]['Tick']
                db.update(data, query.clubID == self.player.club_low_id)