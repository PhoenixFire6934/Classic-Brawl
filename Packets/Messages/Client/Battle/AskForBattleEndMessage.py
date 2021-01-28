from Packets.Messages.Server.Battle.BattleResultMessage import BattleResultMessage
from Packets.Messages.Server.Battle.BattleResult2Message import BattleResult2Message

from Utils.Reader import BSMessageReader


class AskForBattleEndMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client


    def decode(self):
        self.player.battle_result = self.read_Vint()
        self.read_Vint()
        self.player.rank = self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()

        self.player.team = self.read_Vint() #red or blue

        self.read_Vint()

        self.read_string() #Your Name

        self.read_Vint()
        self.Bot1 = self.read_Vint() #bot brawler
        self.read_Vint()
        self.read_Vint() #red or blue
        self.read_Vint()

        self.Bot1N = self.read_string()

        self.read_Vint()
        self.Bot2 = self.read_Vint() #bot brawler
        self.read_Vint()
        self.read_Vint() #red or blue
        self.read_Vint()

        self.Bot2N = self.read_string()

        self.read_Vint()
        self.Bot3 = self.read_Vint() #bot brawler
        self.read_Vint()
        self.read_Vint() #red or blue
        self.read_Vint()

        self.Bot3N = self.read_string()

        self.read_Vint()
        self.Bot4 = self.read_Vint() #bot brawler
        self.read_Vint()
        self.read_Vint() #red or blue
        self.read_Vint()

        self.Bot4N = self.read_string()

        self.read_Vint()
        self.Bot5 = self.read_Vint() #bot brawler
        self.read_Vint()
        self.read_Vint() #red or blue
        self.read_Vint()

        self.Bot5N = self.read_string()

    def process(self):

    	if self.player.rank != 0:
    		BattleResultMessage(self.client, self.player).send()
    	else:
    		if self.player.team == 0:

    			self.player.bot1_n = self.Bot1N
    			self.player.bot2_n = self.Bot2N
    			self.player.bot3_n = self.Bot3N
    			self.player.bot4_n = self.Bot4N
    			self.player.bot5_n = self.Bot5N
    			self.player.bot1 = self.Bot1
    			self.player.bot2 = self.Bot2
    			self.player.bot3 = self.Bot3
    			self.player.bot4 = self.Bot4
    			self.player.bot5 = self.Bot5

    			BattleResult2Message(self.client, self.player).send()
    		else:

    			self.player.bot1_n = self.Bot4N
    			self.player.bot2_n = self.Bot5N
    			self.player.bot3_n = self.Bot3N
    			self.player.bot4_n = self.Bot1N
    			self.player.bot5_n = self.Bot2N
    			self.player.bot1 = self.Bot4
    			self.player.bot2 = self.Bot5
    			self.player.bot3 = self.Bot3
    			self.player.bot4 = self.Bot1
    			self.player.bot5 = self.Bot2
    			BattleResult2Message(self.client, self.player).send()