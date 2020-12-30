from Packets.Messages.Server.Alliance.AllianceChatServerMessage import AllianceChatServerMessage
from Packets.Messages.Server.AllianceBot.AllianceBotChatServerMessage import AllianceBotChatServerMessage
from Packets.Messages.Server.OutOfSyncMessage import OutOfSyncMessage
from Database.DataBase import DataBase

from Utils.Reader import BSMessageReader


class Chat_Message(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client
        self.bot_msg = ''
        self.send_ofs = False
        self.IsAcmd = False

    def decode(self):
        self.msg = self.read_string()

        if self.msg.lower() == '/stats':
            self.bot_msg = f'Server status:\nBuild version: 1.1 (for v26.165)\nFingerprint SHA: {self.player.patch_sha}'
            self.IsAcmd = True

        elif self.msg.lower() == '/reset':
            self.send_ofs = True
            self.IsAcmd = True
            DataBase.replaceValue(self, 'gold', 99999)
            DataBase.replaceValue(self, 'gems', 99999)
            DataBase.replaceValue(self, 'tickets', 99999)

        elif self.msg.lower().startswith('/gems'):
            newGems = self.msg.split(" ", 4)[1:]
            try:
                DataBase.replaceValue(self, 'gems', int(newGems[0]))
                self.send_ofs = True
                self.IsAcmd = True
            except ValueError:
                pass

        elif self.msg.lower().startswith('/gold'):
            newGold = self.msg.split(" ", 4)[1:]
            try:
                DataBase.replaceValue(self, 'gold', int(newGold[0]))
                self.send_ofs = True
                self.IsAcmd = True
            except ValueError:
                pass

        elif self.msg.lower().startswith('/tickets'):
            newTickets = self.msg.split(" ", 7)[1:]
            try:
                DataBase.replaceValue(self, 'tickets', int(newTickets[0]))
                self.send_ofs = True
                self.IsAcmd = True
            except ValueError:
                pass

        elif self.msg.lower().startswith('/starpoints'):
            newStarpoints = self.msg.split(" ", 10)[1:]
            try:
                DataBase.replaceValue(self, 'starpoints', int(newStarpoints[0]))
                self.send_ofs = True
                self.IsAcmd = True
            except ValueError:
                pass

        elif self.msg.lower() == '/help':
            self.bot_msg = 'Club Commands\n/stats - show server status\n/reset - reset all resources\n/gems [int] - add gems to your account, where int is the number of gems\n/gold [int] - add gold to your account, where int is the number of gold\n/tickets [int] - add tickets to your account, where int is the number of tickets\n/starpoints [int] - add starpoints to your account, where int is the number of starpoints'
            self.IsAcmd = True



    def process(self):
        
        if self.IsAcmd == False:
            DataBase.Addmsg(self, 100, 0, self.player.LowID, self.player.name, self.player.ClubRole, self.msg)
            AllianceChatServerMessage(self.client, self.player, self.msg).sendToAll()

        if self.bot_msg != '':
            AllianceBotChatServerMessage(self.client, self.player, self.bot_msg).send()

        if self.send_ofs:
            OutOfSyncMessage(self.client, self.player, 'Changes have been applied').send()