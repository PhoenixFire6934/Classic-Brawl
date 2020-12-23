from Database.DataBase import DataBase

from Utils.Reader import BSMessageReader

class SelectBrawler(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.player.skin_id = self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.player.brawler_id = self.read_Vint()


    def process(self):
        DataBase.replaceValue(self, 'skinID', self.player.skin_id)
        self.player.brawlers_skins[str(self.player.brawler_id)] = self.player.skin_id
        DataBase.replaceValue(self, 'brawlersSkins', self.player.brawlers_skins)

        if self.player.brawler_id == 0:  # Shelly
            self.player.starpower = 76
            self.player.gadget = 255

        elif self.player.brawler_id == 1:  # Colt
            self.player.starpower = 77
            self.player.gadget = 273

        elif self.player.brawler_id == 2:  # Bull
            self.player.starpower = 78
            self.player.gadget = 272

        elif self.player.brawler_id == 3:  # Brock
            self.player.starpower = 79
            self.player.gadget = 245

        elif self.player.brawler_id == 4:  # Rico
            self.player.starpower = 80
            self.player.gadget = 246

        elif self.player.brawler_id == 5:  # Spike
            self.player.starpower = 81
            self.player.gadget = 247

        elif self.player.brawler_id == 6:  # Barley
            self.player.starpower = 82
            self.player.gadget = 273

        elif self.player.brawler_id == 7:  # Jessie
            self.player.starpower = 83
            self.player.gadget = 251

        elif self.player.brawler_id == 8:  # Nita
            self.player.starpower = 84
            self.player.gadget = 249

        elif self.player.brawler_id == 9:  # Dynamike
            self.player.starpower = 85
            self.player.gadget = 258

        elif self.player.brawler_id == 10:  # El Primo
            self.player.starpower = 86
            self.player.gadget = 264

        elif self.player.brawler_id == 11:  # Mortis
            self.player.starpower = 87
            self.player.gadget = 265

        elif self.player.brawler_id == 12:  # Crow
            self.player.starpower = 88
            self.player.gadget = 243

        elif self.player.brawler_id == 13:  # Poco
            self.player.starpower = 89
            self.player.gadget = 267

        elif self.player.brawler_id == 14:  # Bo
            self.player.starpower = 90
            self.player.gadget = 263

        elif self.player.brawler_id == 15:  # Piper
            self.player.starpower = 91
            self.player.gadget = 268

        elif self.player.brawler_id == 16:  # PAM
            self.player.starpower = 92
            self.player.gadget = 257

        elif self.player.brawler_id == 17:  # Tara
            self.player.starpower = 93
            self.player.gadget = 266

        elif self.player.brawler_id == 18:  # Darryl
            self.player.starpower = 94
            self.player.gadget = 260

        elif self.player.brawler_id == 19:  # Penny
            self.player.starpower = 99
            self.player.gadget = 248

        elif self.player.brawler_id == 20:  # Frank
            self.player.starpower = 104
            self.player.gadget = 261

        elif self.player.brawler_id == 21:  # Gene
            self.player.starpower = 109
            self.player.gadget = 252

        elif self.player.brawler_id == 22:  # Tick
            self.player.starpower = 114
            self.player.gadget = 253

        elif self.player.brawler_id == 23:  # Leon
            self.player.starpower = 119
            self.player.gadget = 276

        elif self.player.brawler_id == 24:  # Rosa
            self.player.starpower = 124
            self.player.gadget = 242

        elif self.player.brawler_id == 25:  # Carl
            self.player.starpower = 129
            self.player.gadget = 262

        elif self.player.brawler_id == 26:  # Bibi
            self.player.starpower = 134
            self.player.gadget = 275

        elif self.player.brawler_id == 27:  # 8-Bit
            self.player.starpower = 168
            self.player.gadget = 259

        elif self.player.brawler_id == 28:  # Sandy
            self.player.starpower = 186
            self.player.gadget = 270

        elif self.player.brawler_id == 29:  # Bea
            self.player.starpower = 192
            self.player.gadget = 271

        elif self.player.brawler_id == 30:  # EMZ
            self.player.starpower = 198
            self.player.gadget = 274

        elif self.player.brawler_id == 31:  # Mr. P
            self.player.starpower = 204
            self.player.gadget = 269

        elif self.player.brawler_id == 32:  # Max
            self.player.starpower = 210
            self.player.gadget = 254

        elif self.player.brawler_id == 34:  # Jacky
            self.player.starpower = 222
            self.player.gadget = 256

        elif self.player.brawler_id == 35:  # Gale
            self.player.starpower = 228
            self.player.gadget = 277

        elif self.player.brawler_id == 36:  # Nani
            self.player.starpower = 234
            self.player.gadget = 278

        elif self.player.brawler_id == 37:  # Sprout
            self.player.starpower = 240
            self.player.gadget = 244

        DataBase.replaceValue(self, 'starpower', self.player.starpower)
        DataBase.replaceValue(self, 'gadget', self.player.gadget)

        DataBase.replaceValue(self, 'brawlerID', self.player.brawler_id)
