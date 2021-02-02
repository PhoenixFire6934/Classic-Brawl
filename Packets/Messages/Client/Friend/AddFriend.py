from Utils.Reader import BSMessageReader

from Packets.Messages.Server.Friend.Events.AddFriendFailedMessage import AddFriendFailedMessage
from Packets.Messages.Server.Friend.FriendListUpdateMessage import FriendListUpdateMessage


class AddFriend(BSMessageReader):

    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.HighID = self.read_int()
        self.LowID = self.read_int()

    def process(self):
        print(self.HighID, self.LowID)
        FriendListUpdateMessage(self.client, self.player, self.LowID).send()
        #AddFriendFailedMessage(self.client, self.player).send()