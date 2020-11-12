from Packets.Messages.Server.Gameroom.TeamGameroomDataMessage import TeamGameroomDataMessage
from Database.DataBase import DataBase

from Utils.Reader import BSMessageReader


class TeamChangeMemberSettingsMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.Unk = self.read_Vint()
        self.read_Vint()
        self.BrawlerSkinId = self.read_Vint()

    def process(self):
        if self.Unk != 23:
            if self.BrawlerSkinId == 0:
                self.player.brawlerID = 0

            elif self.BrawlerSkinId == 29:
                self.player.brawlerID = 0

            elif self.BrawlerSkinId == 52:
                self.player.brawlerID = 0

            elif self.BrawlerSkinId == 122:
                self.player.brawlerID = 0

            elif self.BrawlerSkinId == 159:
                self.player.brawlerID = 0

            elif self.BrawlerSkinId == 14:
                self.player.brawlerID = 8

            elif self.BrawlerSkinId == 15:
                self.player.brawlerID = 8

            elif self.BrawlerSkinId == 60:
                self.player.brawlerID = 8

            elif self.BrawlerSkinId == 79:
                self.player.brawlerID = 8

            elif self.BrawlerSkinId == 148:
                self.player.brawlerID = 8

            elif self.BrawlerSkinId == 1:
                self.player.brawlerID = 1

            elif self.BrawlerSkinId == 2:
                self.player.brawlerID = 1

            elif self.BrawlerSkinId == 69:
                self.player.brawlerID = 1

            elif self.BrawlerSkinId == 103:
                self.player.brawlerID = 1

            elif self.BrawlerSkinId == 135:
                self.player.brawlerID = 1

            elif self.BrawlerSkinId == 3:
                self.player.brawlerID = 2

            elif self.BrawlerSkinId == 25:
                self.player.brawlerID = 2

            elif self.BrawlerSkinId == 64:
                self.player.brawlerID = 2

            elif self.BrawlerSkinId == 102:
                self.player.brawlerID = 2

            elif self.BrawlerSkinId == 178:
                self.player.brawlerID = 2

            elif self.BrawlerSkinId == 13:
                self.player.brawlerID = 7

            elif self.BrawlerSkinId == 44:
                self.player.brawlerID = 7

            elif self.BrawlerSkinId == 47:
                self.player.brawlerID = 7

            elif self.BrawlerSkinId == 123:
                self.player.brawlerID = 7

            elif self.BrawlerSkinId == 162:
                self.player.brawlerID = 7

            elif self.BrawlerSkinId == 174:
                self.player.brawlerID = 7

            elif self.BrawlerSkinId == 4:
                self.player.brawlerID = 3

            elif self.BrawlerSkinId == 5:
                self.player.brawlerID = 3

            elif self.BrawlerSkinId == 58:
                self.player.brawlerID = 3

            elif self.BrawlerSkinId == 72:
                self.player.brawlerID = 3

            elif self.BrawlerSkinId == 91:
                self.player.brawlerID = 3

            elif self.BrawlerSkinId == 6:
                self.player.brawlerID = 9

            elif self.BrawlerSkinId == 56:
                self.player.brawlerID = 9

            elif self.BrawlerSkinId == 57:
                self.player.brawlerID = 9

            elif self.BrawlerSkinId == 97:
                self.player.brawlerID = 9

            elif self.BrawlerSkinId == 160:
                self.player.brawlerID = 9

            elif self.BrawlerSkinId == 22:
                self.player.brawlerID = 14

            elif self.BrawlerSkinId == 94:
                self.player.brawlerID = 14

            elif self.BrawlerSkinId == 98:
                self.player.brawlerID = 14

            elif self.BrawlerSkinId == 99:
                self.player.brawlerID = 14

            elif self.BrawlerSkinId == 163:
                self.player.brawlerID = 14

            elif self.BrawlerSkinId == 86:
                self.player.brawlerID = 22

            elif self.BrawlerSkinId == 106:
                self.player.brawlerID = 27

            elif self.BrawlerSkinId == 109:
                self.player.brawlerID = 27

            elif self.BrawlerSkinId == 143:
                self.player.brawlerID = 27

            elif self.BrawlerSkinId == 119:
                self.player.brawlerID = 30

            elif self.BrawlerSkinId == 167:
                self.player.brawlerID = 30

            elif self.BrawlerSkinId == 7:
                self.player.brawlerID = 10

            elif self.BrawlerSkinId == 28:
                self.player.brawlerID = 10

            elif self.BrawlerSkinId == 30:
                self.player.brawlerID = 10

            elif self.BrawlerSkinId == 128:
                self.player.brawlerID = 10

            elif self.BrawlerSkinId == 12:
                self.player.brawlerID = 6

            elif self.BrawlerSkinId == 27:
                self.player.brawlerID = 6

            elif self.BrawlerSkinId == 59:
                self.player.brawlerID = 6

            elif self.BrawlerSkinId == 90:
                self.player.brawlerID = 6

            elif self.BrawlerSkinId == 92:
                self.player.brawlerID = 6

            elif self.BrawlerSkinId == 116:
                self.player.brawlerID = 6

            elif self.BrawlerSkinId == 21:
                self.player.brawlerID = 13

            elif self.BrawlerSkinId == 71:
                self.player.brawlerID = 13

            elif self.BrawlerSkinId == 140:
                self.player.brawlerID = 13

            elif self.BrawlerSkinId == 77:
                self.player.brawlerID = 24

            elif self.BrawlerSkinId == 9:
                self.player.brawlerID = 4

            elif self.BrawlerSkinId == 26:
                self.player.brawlerID = 4

            elif self.BrawlerSkinId == 68:
                self.player.brawlerID = 4

            elif self.BrawlerSkinId == 130:
                self.player.brawlerID = 4

            elif self.BrawlerSkinId == 171:
                self.player.brawlerID = 4

            elif self.BrawlerSkinId == 34:
                self.player.brawlerID = 18

            elif self.BrawlerSkinId == 70:
                self.player.brawlerID = 18

            elif self.BrawlerSkinId == 158:
                self.player.brawlerID = 18

            elif self.BrawlerSkinId == 41:
                self.player.brawlerID = 19

            elif self.BrawlerSkinId == 61:
                self.player.brawlerID = 19

            elif self.BrawlerSkinId == 88:
                self.player.brawlerID = 19

            elif self.BrawlerSkinId == 165:
                self.player.brawlerID = 19

            elif self.BrawlerSkinId == 73:
                self.player.brawlerID = 25

            elif self.BrawlerSkinId == 93:
                self.player.brawlerID = 25

            elif self.BrawlerSkinId == 104:
                self.player.brawlerID = 25

            elif self.BrawlerSkinId == 132:
                self.player.brawlerID = 25

            elif self.BrawlerSkinId == 134:
                self.player.brawlerID = 25

            elif self.BrawlerSkinId == 142:
                self.player.brawlerID = 34

            elif self.BrawlerSkinId == 176:
                self.player.brawlerID = 34

            elif self.BrawlerSkinId == 23:
                self.player.brawlerID = 15

            elif self.BrawlerSkinId == 108:
                self.player.brawlerID = 15

            elif self.BrawlerSkinId == 120:
                self.player.brawlerID = 15

            elif self.BrawlerSkinId == 147:
                self.player.brawlerID = 15

            elif self.BrawlerSkinId == 24:
                self.player.brawlerID = 16

            elif self.BrawlerSkinId == 179:
                self.player.brawlerID = 16

            elif self.BrawlerSkinId == 42:
                self.player.brawlerID = 20

            elif self.BrawlerSkinId == 45:
                self.player.brawlerID = 20

            elif self.BrawlerSkinId == 125:
                self.player.brawlerID = 20

            elif self.BrawlerSkinId == 81:
                self.player.brawlerID = 26

            elif self.BrawlerSkinId == 146:
                self.player.brawlerID = 26

            elif self.BrawlerSkinId == 114:
                self.player.brawlerID = 29

            elif self.BrawlerSkinId == 139:
                self.player.brawlerID = 29

            elif self.BrawlerSkinId == 156:
                self.player.brawlerID = 36

            elif self.BrawlerSkinId == 18:
                self.player.brawlerID = 11

            elif self.BrawlerSkinId == 50:
                self.player.brawlerID = 11

            elif self.BrawlerSkinId == 63:
                self.player.brawlerID = 11

            elif self.BrawlerSkinId == 75:
                self.player.brawlerID = 11

            elif self.BrawlerSkinId == 173:
                self.player.brawlerID = 11

            elif self.BrawlerSkinId == 32:
                self.player.brawlerID = 17

            elif self.BrawlerSkinId == 111:
                self.player.brawlerID = 17

            elif self.BrawlerSkinId == 145:
                self.player.brawlerID = 17

            elif self.BrawlerSkinId == 67:
                self.player.brawlerID = 21

            elif self.BrawlerSkinId == 117:
                self.player.brawlerID = 21

            elif self.BrawlerSkinId == 172:
                self.player.brawlerID = 21

            elif self.BrawlerSkinId == 127:
                self.player.brawlerID = 32

            elif self.BrawlerSkinId == 137:
                self.player.brawlerID = 32

            elif self.BrawlerSkinId == 121:
                self.player.brawlerID = 31

            elif self.BrawlerSkinId == 152:
                self.player.brawlerID = 31

            elif self.BrawlerSkinId == 157:
                self.player.brawlerID = 37

            elif self.BrawlerSkinId == 177:
                self.player.brawlerID = 37

            elif self.BrawlerSkinId == 10:
                self.player.brawlerID = 5

            elif self.BrawlerSkinId == 11:
                self.player.brawlerID = 5

            elif self.BrawlerSkinId == 96:
                self.player.brawlerID = 5

            elif self.BrawlerSkinId == 19:
                self.player.brawlerID = 12

            elif self.BrawlerSkinId == 20:
                self.player.brawlerID = 12

            elif self.BrawlerSkinId == 49:
                self.player.brawlerID = 12

            elif self.BrawlerSkinId == 95:
                self.player.brawlerID = 12

            elif self.BrawlerSkinId == 100:
                self.player.brawlerID = 12

            elif self.BrawlerSkinId == 101:
                self.player.brawlerID = 12

            elif self.BrawlerSkinId == 62:
                self.player.brawlerID = 23

            elif self.BrawlerSkinId == 110:
                self.player.brawlerID = 23

            elif self.BrawlerSkinId == 126:
                self.player.brawlerID = 23

            elif self.BrawlerSkinId == 131:
                self.player.brawlerID = 23

            elif self.BrawlerSkinId == 113:
                self.player.brawlerID = 28

            elif self.BrawlerSkinId == 118:
                self.player.brawlerID = 28

            elif self.BrawlerSkinId == 155:
                self.player.brawlerID = 35

            elif self.BrawlerSkinId == 180:
                self.player.brawlerID = 35


            if self.player.brawlerID == 0: #Shelly
                self.player.starpower = 76
                self.player.gadget = 255

            elif self.player.brawlerID == 1: #Colt
                self.player.starpower = 77
                self.player.gadget = 273

            elif self.player.brawlerID == 2: #Bull
                self.player.starpower = 78
                self.player.gadget = 272

            elif self.player.brawlerID == 3: #Brock
                self.player.starpower = 79
                self.player.gadget = 245

            elif self.player.brawlerID == 4: #Rico
                self.player.starpower = 80
                self.player.gadget = 246

            elif self.player.brawlerID == 5: #Spike
                self.player.starpower = 81
                self.player.gadget = 247

            elif self.player.brawlerID == 6: #Barley
                self.player.starpower = 82
                self.player.gadget = 273

            elif self.player.brawlerID == 7: #Jessie
                self.player.starpower = 83
                self.player.gadget = 251

            elif self.player.brawlerID == 8: #Nita
                self.player.starpower = 84
                self.player.gadget = 249

            elif self.player.brawlerID == 9: #Dynamike
                self.player.starpower = 85
                self.player.gadget = 258

            elif self.player.brawlerID == 10: #El Primo
                self.player.starpower = 86
                self.player.gadget = 264

            elif self.player.brawlerID == 11: #Mortis
                self.player.starpower = 87
                self.player.gadget = 265

            elif self.player.brawlerID == 12: #Crow
                self.player.starpower = 88
                self.player.gadget = 243

            elif self.player.brawlerID == 13: #Poco
                self.player.starpower = 89
                self.player.gadget = 267

            elif self.player.brawlerID == 14: #Bo
                self.player.starpower = 90
                self.player.gadget = 263

            elif self.player.brawlerID == 15: #Piper
                self.player.starpower = 91
                self.player.gadget = 268

            elif self.player.brawlerID == 16: #PAM
                self.player.starpower = 92
                self.player.gadget = 257

            elif self.player.brawlerID == 17: #Tara
                self.player.starpower = 93
                self.player.gadget = 266

            elif self.player.brawlerID == 18: #Darryl
                self.player.starpower = 94
                self.player.gadget = 260

            elif self.player.brawlerID == 19: #Penny
                self.player.starpower = 99
                self.player.gadget = 248

            elif self.player.brawlerID == 20: #Frank
                self.player.starpower = 104
                self.player.gadget = 261

            elif self.player.brawlerID == 21: #Gene
                self.player.starpower = 109
                self.player.gadget = 252

            elif self.player.brawlerID == 22: #Tick
                self.player.starpower = 114
                self.player.gadget = 253

            elif self.player.brawlerID == 23: #Leon
                self.player.starpower = 119
                self.player.gadget = 276

            elif self.player.brawlerID == 24: #Rosa
                self.player.starpower = 124
                self.player.gadget = 242

            elif self.player.brawlerID == 25: #Carl
                self.player.starpower = 129
                self.player.gadget = 262

            elif self.player.brawlerID == 26: #Bibi
                self.player.starpower = 134
                self.player.gadget = 275

            elif self.player.brawlerID == 27: #8-Bit
                self.player.starpower = 168
                self.player.gadget = 259

            elif self.player.brawlerID == 28: #Sandy
                self.player.starpower = 186
                self.player.gadget = 270

            elif self.player.brawlerID == 29: #Bea
                self.player.starpower = 192
                self.player.gadget = 271

            elif self.player.brawlerID == 30: #EMZ
                self.player.starpower = 198
                self.player.gadget = 274

            elif self.player.brawlerID == 31: #Mr. P
                self.player.starpower = 204
                self.player.gadget = 269

            elif self.player.brawlerID == 32: #Max
                self.player.starpower = 210
                self.player.gadget = 254

            elif self.player.brawlerID == 34: #Jacky
                self.player.starpower = 222
                self.player.gadget = 256

            elif self.player.brawlerID == 35: #Gale
                self.player.starpower = 228
                self.player.gadget = 277

            elif self.player.brawlerID == 36: #Nani
                self.player.starpower = 234
                self.player.gadget = 278

            elif self.player.brawlerID == 37: #Sprout
                self.player.starpower = 240
                self.player.gadget = 244

            DataBase.replaceValue(self, 'starpower', self.player.starpower)
            DataBase.replaceValue(self, 'gadget', self.player.gadget)

            TeamGameroomDataMessage(self.client, self.player).send()