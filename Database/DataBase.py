import json
from os import read
import string
import random
from typing import Dict
from Utils.Helpers import Helpers
from Files.CsvLogic.Characters import Characters

class DataBase:

    def loadAccount(self):
        with open('data.db', 'r') as read_data:
            for line in read_data.readlines():

                json_data = json.loads(line)
                dict = json.loads(json.dumps(json_data))  # loading and dumping json data from file
                
                if self.player.Token in dict:
                    self.TotalTrophies = 0

                    self.player.LowID = dict[str(self.player.Token)]["lowID"]
                    self.player.ClubID = dict[str(self.player.Token)]["clubID"]
                    self.player.ClubRole = dict[str(self.player.Token)]["clubRole"]
                    self.player.name = dict[str(self.player.Token)]["name"]
                    self.player.gems = dict[str(self.player.Token)]["gems"]
                    self.player.gold = dict[str(self.player.Token)]["gold"]
                    self.player.starPoints = dict[str(self.player.Token)]["starpoints"]
                    self.player.tickets = dict[str(self.player.Token)]["tickets"]
                    self.player.brawlerID = dict[str(self.player.Token)]["brawlerID"]
                    self.player.skinID = dict[str(self.player.Token)]["skinID"]
                    self.player.BrawlersTrophies = dict[str(self.player.Token)]["brawlersTrophies"]
                    self.player.BrawlersTrophiesForRank = dict[str(self.player.Token)]["brawlersTrophiesForRank"]
                    
                    for BrawlerID in self.player.BrawlersTrophies.keys():
                        self.TotalTrophies += self.player.BrawlersTrophies[BrawlerID]

                    if self.TotalTrophies < dict[str(self.player.Token)]["highesttrophies"]:
                        self.player.maxTrophiesReached = dict[str(self.player.Token)]["highesttrophies"]
                    else:
                        self.player.maxTrophiesReached = self.TotalTrophies
                        self.player.trophies = self.TotalTrophies

                    self.player.profileIcon = dict[str(self.player.Token)]["profileIcon"]
                    self.player.namecolor = dict[str(self.player.Token)]["namecolor"]
                    self.player.brawlBoxes = dict[str(self.player.Token)]["brawlBoxes"]
                    self.player.bigBoxes = dict[str(self.player.Token)]["bigBoxes"]
                    # self.player.contentCreator = dict[str(self.player.Token)]["contentCreator"]
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
                    self.player.gadget = dict[str(self.player.Token)]["gadget"]
                    self.player.starpower = dict[str(self.player.Token)]["starpower"]
                    self.player.DoNotDistrubMessage = dict[str(self.player.Token)]["DoNotDistrub"]
                    self.player.roomID = dict[str(self.player.Token)]["roomID"]
    
    def loadOtherAccount(self, plrLow_id):
        with open('data.db', 'r') as read_data:
            for line in read_data.readlines():

                json_data = json.loads(line)
                dict = json.loads(json.dumps(json_data))  # loading and dumping json data from file

                for playertoken, info in dict.items():
                    if plrLow_id == info["lowID"]:
                        self.TotalTrophies = 0

                        self.ClubID = info["clubID"]
                        self.ClubRole = info["clubRole"]
                        self.name = info["name"]
                        self.gems = info["gems"]
                        self.gold = info["gold"]
                        self.starPoints = info["starpoints"]
                        self.tickets = info["tickets"]
                        self.BrawlersCount = Characters.get_brawlers_id()
                        self.brawlerID = info["brawlerID"]
                        self.skinID = info["skinID"]
                        self.BrawlersTrophies = info["brawlersTrophies"]
                        self.BrawlersTrophiesForRank = info["brawlersTrophiesForRank"]

                        for BrawlerID in self.BrawlersTrophies.keys():
                            self.TotalTrophies += self.BrawlersTrophies[BrawlerID]

                        if self.TotalTrophies < info["highesttrophies"]:
                            self.maxTrophiesReached = info["highesttrophies"]
                        else:
                            self.maxTrophiesReached = self.TotalTrophies
                            self.trophies = self.TotalTrophies

                        self.trophies = info["trophies"]
                        self.profileIcon = info["profileIcon"]
                        self.brawlBoxes = info["brawlBoxes"]
                        self.bigBoxes = info["bigBoxes"]
                        # self.contentCreator = info["contentCreator"]
                        self.shellySkin = info["shellySkin"]
                        self.nitaSkin = info["nitaSkin"]
                        self.coltSkin = info["coltSkin"]
                        self.bullSkin = info["bullSkin"]
                        self.jessieSkin = info["jessieSkin"]
                        self.brockSkin = info["brockSkin"]
                        self.dynamikeSkin = info["dynamikeSkin"]
                        self.boSkin = info["boSkin"]
                        self.elprimoSkin = info["elprimoSkin"]
                        self.barleySkin = info["barleySkin"]
                        self.pocoSkin = info["pocoSkin"]
                        self.ricoSkin = info["ricoSkin"]
                        self.darrylSkin = info["darrylSkin"]
                        self.pennySkin = info["pennySkin"]
                        self.piperSkin = info["piperSkin"]
                        self.pamSkin = info["pamSkin"]
                        self.frankSkin = info["frankSkin"]
                        self.mortisSkin = info["mortisSkin"]
                        self.taraSkin = info["taraSkin"]
                        self.spikeSkin = info["spikeSkin"]
                        self.crowSkin = info["crowSkin"]
                        self.geneSkin = info["geneSkin"]
                        self.tickSkin = info["tickSkin"]
                        self.leonSkin = info["leonSkin"]
                        self.rosaSkin = info["rosaSkin"]
                        self.carlSkin = info["carlSkin"]
                        self.bibiSkin = info["bibiSkin"]
                        self.bitSkin = info["8bitSkin"]
                        self.sandySkin = info["sandySkin"]
                        self.beaSkin = info["beaSkin"]
                        self.emzSkin = info["emzSkin"]
                        self.mrpSkin = info["mrpSkin"]
                        self.maxSkin = info["maxSkin"]
                        self.jackySkin = info["jackySkin"]
                        self.galeSkin = info["galeSkin"]
                        self.naniSkin = info["naniSkin"]
                        self.sproutSkin = info["sproutSkin"]
                        self.namecolor = info["namecolor"]
                        self.gadget = info["gadget"]
                        self.starpower = info["starpower"]
                        self.DoNotDistrubMessage = info["DoNotDistrub"]
                        self.roomID = info["roomID"]

    def createAccount(self):
        data = {
            self.player.Token: {
                "lowID": self.player.LowID,
                "clubID": 0,
                "clubRole": 0,
                "name": self.player.name,
                "gems": self.player.gems,
                "gold": self.player.gold,
                "starpoints": self.player.starPoints,
                "tickets": self.player.tickets,
                "brawlerID": 0,
                "skinID": 0,
                "highesttrophies": self.player.trophies,
                "trophies": self.player.trophies,
                "profileIcon": 0,
                "namecolor": 0,
                "brawlBoxes": self.player.brawlBoxes,
                "bigBoxes": self.player.bigBoxes,
                # "contentCreator": "",
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
                "roomID": 0,
                "brawlersTrophies": self.player.BrawlersTrophies,
                "brawlersTrophiesForRank": self.player.BrawlersTrophiesForRank
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


        # Alliance function
    
    def createClub(self, clubid):
        data = {
            clubid: {
                "name": self.clubName,                          
                "description": self.clubdescription,
                "region": "RO",
                "badgeID": self.clubbadgeID,
                "type": self.clubtype,
                "trophiesneeded": self.clubtrophiesneeded,
                "friendlyfamily": self.clubfriendlyfamily,
                "trophies": self.player.trophies,
                "members": {
                    "totalmembers": 1,
                    str(self.player.LowID): self.player.name
                }
            }
        }

        msgData = {
            clubid: {
                "Total": 1,
                "1": {
                    "Event": 2,
                    "Tick": 1,
                    "PlayerID": self.player.LowID,
                    "PlayerName": self.player.name,
                    "PlayerRole": 2,
                    "Message": "Welcome to you're new club!"
                }
            }
        }

        with open('club.db', 'a+') as data_file:
            json.dump(data, data_file)  # writing data for new club
            data_file.write('\n')  # writing a new line

        with open('chat.db', 'a+') as data_file:
            json.dump(msgData, data_file)  # writing data for new club
            data_file.write('\n')  # writing a new line

    def loadClub(self, clubid):
        self.plrids = []
        self.clubidstr = str(clubid)
        with open('club.db', 'r') as read_data:
            for line in read_data.readlines():
                
                json_data = json.loads(line)
                dict = json.loads(json.dumps(json_data))

                if self.clubidstr in dict:
                    self.clubName = dict[str(self.clubidstr)]["name"]
                    self.clubdescription = dict[str(self.clubidstr)]["description"]
                    self.clubregion = dict[str(self.clubidstr)]["region"]
                    self.clubbadgeID = dict[str(self.clubidstr)]["badgeID"]
                    self.clubtype = dict[str(self.clubidstr)]["type"]
                    self.clubtrophiesneeded = dict[str(self.clubidstr)]["trophiesneeded"]
                    self.clubfriendlyfamily = dict[str(self.clubidstr)]["friendlyfamily"]
                    self.clubtrophies = dict[str(self.clubidstr)]["trophies"]
                    self.clubmembercount = dict[str(self.clubidstr)]["members"]["totalmembers"]
                    for plridentifier, data in dict[str(self.clubidstr)]["members"].items():
                        if plridentifier != "totalmembers":
                            self.plrids.append(int(plridentifier))
    

    def replaceClubValue(self, target, inf1, inf2, inf3, inf4, inf5):
        with open('club.db', 'r+') as file:
            list = []

            for line in file.readlines():

                json_data = json.loads(line)
                dict = json.loads(json.dumps(json_data))  # loading and dumping json data from file

                print("Scaning...", target)
                if str(target) in dict:
                    dict[str(target)]['description'] = inf1
                    dict[str(target)]['badgeID'] = inf2
                    dict[str(target)]['type'] = inf3
                    dict[str(target)]['trophiesneeded'] = inf4
                    dict[str(target)]['friendlyfamily'] = inf5
                    print("Done!")
                list.append(dict)
                file.close()

        with open('club.db', 'w') as o:
            for i in list:
                o.write(str(i).replace("'", '"') + '\n')
            o.close()

    def CountClub(self, minMembers, maxMembers, clubType, maxListLength):
        self.AllianceCount = 0
        with open('club.db', 'r') as read_data:
            for club in read_data.readlines():

                clubData = json.loads(club)
                dict = json.loads(json.dumps(clubData))

                for name, info in dict.items():
                    if info["members"]["totalmembers"] >= minMembers and info["members"]["totalmembers"] < maxMembers and info["type"] <= clubType and self.AllianceCount <= maxListLength:
                        self.AllianceCount += 1

    def AddMember(self, clubid, PlayerLow_ID, plrName, action):
        PlayerID = str(PlayerLow_ID)
        PlayerName = plrName
        AllianceID = clubid
        Action = action
        newData = []

        if Action == 0:
            with open('club.db', 'r') as file:
                for club in file.readlines():
                    
                    plrData = json.loads(club)
                    dict = json.loads(json.dumps(plrData)) # loading and dumping json data from file

                    for Identifier, data in dict.items():
                        if int(Identifier) != AllianceID:
                            newData.append(club)
                                                                                                    
        elif Action == 1:
            with open('club.db', 'r+') as file:
                for line in file.readlines():

                    json_data = json.loads(line)
                    dict = json.loads(json.dumps(json_data))

                    for Identifier, data in dict.items():
                        if int(Identifier) == AllianceID:
                            dict[Identifier]['members']['totalmembers'] += 1    
                            dict[Identifier]['members'][PlayerID] = PlayerName

                    newData.append(json.dumps(dict))
                    file.close()  
            

        elif Action == 2:
            with open('club.db', 'r+') as file:
                for line in file.readlines():

                    json_data = json.loads(line)
                    dict = json.loads(json.dumps(json_data))

                    for Identifier, data in dict.items():
                        if int(Identifier) == AllianceID:
                            dict[Identifier]['members']['totalmembers'] -= 1
                            dict[Identifier]['members'].pop(PlayerID)

                    newData.append(json.dumps(dict)) 
                    file.close()        

        with open('club.db', 'w') as o:
            o.writelines('\n'.join(newData))
            o.close()       
            
    def GetMemberData(self, Low_id):
        with open('data.db', 'r') as read_data:
            for plrtoken in read_data.readlines():

                plrData = json.loads(plrtoken)
                dict = json.loads(json.dumps(plrData))

                for playertoken, data in dict.items():
                    if Low_id == data["lowID"]:
                        self.lowplrid = data["lowID"]
                        self.plrrole = data["clubRole"]
                        self.plrtrophies = data["trophies"]
                        self.plrname = data["name"]
                        self.plricon = data["profileIcon"]
                        self.plrnamecolor = data["namecolor"]
    
    # Club message

    def GetmsgCount(self, clubID):
        with open('chat.db', 'r') as read_data:
            for line in read_data.readlines():
                
                json_data = json.loads(line)
                dict = json.loads(json.dumps(json_data))

                if str(clubID) in dict:
                    self.MessageCount = dict[str(clubID)]['Total']
                    if self.MessageCount != 0:
                        self.player.messageTick = dict[str(clubID)][str(self.MessageCount)]['Tick'] + 1

    def Addmsg(self, event, tick, Low_id, name, role, msg):
        self.updatedDict = []
        index = 0
        with open('chat.db', 'r+') as file:
            for line in file.readlines():

                json_data = json.loads(line)
                dict = json.loads(json.dumps(json_data))

                for clubIdentifier, data in dict.items():

                    if int(clubIdentifier) == self.player.ClubID:

                        for i in range(1, dict[str(clubIdentifier)]['Total'] + 1):
                            index += 1

                            if index == dict[str(clubIdentifier)]['Total']:
                                
                                if event == 100:
                                    dict[str(clubIdentifier)][str(i + 1)] = {"Event": 2, "Tick": dict[str(clubIdentifier)][str(i)]['Tick'] + 1, "PlayerID": Low_id, "PlayerName": name, "PlayerRole": role, "Message": msg}
                                    dict[str(clubIdentifier)]['Total'] = i + 1
                                    self.player.ClubMessageCount = dict[str(clubIdentifier)]['Total'] = i + 1
                                    self.player.messageTick = dict[str(clubIdentifier)][str(i)]['Tick']
                                    break
                                else:
                                    dict[str(clubIdentifier)][str(i + 1)] = {"Event": event, "Tick": dict[str(clubIdentifier)][str(i)]['Tick'] + 1, "PlayerID": Low_id, "PlayerName": name, "PlayerRole": role, "Message": msg}
                                    dict[str(clubIdentifier)]['Total'] = i + 1
                                    self.player.ClubMessageCount = dict[str(clubIdentifier)]['Total'] = i + 1
                                    self.player.messageTick = dict[str(clubIdentifier)][str(i)]['Tick']
                                    break

                self.updatedDict.append(json.dumps(dict))            
                file.close()
        
        with open('chat.db', 'w') as o:
            o.writelines('\n'.join(self.updatedDict))
            o.write('\n')
            o.close()