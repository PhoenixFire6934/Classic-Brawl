from ByteStream.Reader import Reader
from Utils.Helpers import Helpers
from Protocol.LogicCommandManager import commands

class EndClientTurnMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.client = client
        self.player = player

    def decode(self):
        self.readVInt()
        self.readVInt()
        self.readVInt()
        self.tick = self.readVInt()
        if self.tick != 0:
            self.commandID = self.readVInt()


    def process(self, db):
        if self.tick != 0:
            if self.commandID in commands:
                command = commands[self.commandID]
                try:
                    command.decode(self)
                    command.process(self, db)
                except AttributeError:
                    command(self.client, self.player).send() # Exception for OutOfSyncMessage
            else:
                print(f'{Helpers.cyan}[CLIENT] Unhandled Command! ID: {self.commandID}')