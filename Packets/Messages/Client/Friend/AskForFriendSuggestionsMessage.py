from Packets.Messages.Server.Friend.AddableFriendsMessage import AddableFriendsMessage
from Utils.Reader import BSMessageReader

class AskForFriendSuggestionsMessage(BSMessageReader):

    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        pass

    def process(self):
        AddableFriendsMessage(self.client, self.player).send()