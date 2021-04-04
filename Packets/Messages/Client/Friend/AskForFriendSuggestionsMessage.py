from Packets.Messages.Server.Friend.AddableFriendsMessage import AddableFriendsMessage
from Database.DatabaseManager import DataBase
from Utils.Reader import BSMessageReader

class AskForFriendSuggestionsMessage(BSMessageReader):

    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        pass

    def process(self):
        def by_trophy(plr):
                return plr['trophies']
                
        players = DataBase.getAllPlayers(self)
        players.sort(key = by_trophy, reverse=True)
        AddableFriendsMessage(self.client, self.player, players).send()