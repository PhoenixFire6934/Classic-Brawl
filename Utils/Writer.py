from tinydb import database
from Database.DatabaseManager import DataBase
from Utils.Config import Config

packet_settings = Config.GetValue()


class Writer:
    def __init__(self, client, endian: str = 'big'):
        self.client = client
        self.endian = endian
        self.buffer = b''

    def writeInt(self, data, length=4):
        self.buffer += data.to_bytes(length, 'big')

    def writeUInteger(self, integer: int, length: int = 1):
        self.buffer += integer.to_bytes(length, self.endian, signed=False)

    def writeArrayVint(self, data):
        for x in data:
            self.writeVint(x)

    def writeUInt8(self, integer: int):
        self.writeUInteger(integer)

    def writeBoolean(self, boolean: bool):
        if boolean:
            self.writeUInt8(1)
        else:
            self.writeUInt8(0)

    def writeHexa(self, data):
        if data:
            if data.startswith('0x'):
                data = data[2:]

            self.buffer += bytes.fromhex(''.join(data.split()).replace('-', ''))

    def send(self):
        self.encode()
        packet = self.buffer
        self.buffer = self.id.to_bytes(2, 'big', signed=True)
        self.writeInt(len(packet), 3)
        if hasattr(self, 'version'):
            self.writeInt16(self.version)
        else:
            self.writeInt16(0)
        self.buffer += packet + b'\xff\xff\x00\x00\x00\x00\x00'
        self.client.send(self.buffer)
        if packet_settings["ShowPacketsInLog"] == True:
            print(self.id, self.__class__.__name__)

    def sendToAll(self):
        if self.player.club_low_id != 0:
            self.encode()
            packet = self.buffer
            self.buffer = self.id.to_bytes(2, 'big', signed=True)
            self.writeInt(len(packet), 3)
            if hasattr(self, 'version'):
                self.writeInt16(self.version)
            else:
                self.writeInt16(0)
            self.buffer += packet + b'\xff\xff\x00\x00\x00\x00\x00'
            for Client in range(self.player.ClientDict["ClientCounts"]):
                for client_id, value in self.player.ClientDict["Clients"].items():
                    DataBase.loadOtherAccount(self, int(client_id))
                    if self.ClubID == self.player.club_low_id:
                        self.player.ClientDict["Clients"][str(client_id)]["SocketInfo"].send(self.buffer)
                break
            if packet_settings["ShowPacketsInLog"] == True:
                print(self.id, self.__class__.__name__)

    def sendToOthers(self):
        self.encode()
        packet = self.buffer
        self.buffer = self.id.to_bytes(2, 'big', signed=True)
        self.writeInt(len(packet), 3)
        if hasattr(self, 'version'):
            self.writeInt16(self.version)
        else:
            self.writeInt16(0)
        self.buffer += packet + b'\xff\xff\x00\x00\x00\x00\x00'
        for Client in range(self.player.ClientDict["ClientCounts"]):
            for client_id, value in self.player.ClientDict["Clients"].items():
                DataBase.loadOtherAccount(self, int(client_id))
                if client_id != self.player.low_id and self.ClubID == self.player.club_low_id:
                    self.player.ClientDict["Clients"][str(client_id)]["SocketInfo"].send(self.buffer)
            break
        if packet_settings["ShowPacketsInLog"] == True:
            print(self.id, self.__class__.__name__)

    def sendWithLowID(self, low_id):
        try:
            self.encode()
            packet = self.buffer
            self.buffer = self.id.to_bytes(2, 'big', signed=True)
            self.writeInt(len(packet), 3)
            if hasattr(self, 'version'):
                self.writeInt16(self.version)
            else:
                self.writeInt16(0)
            self.buffer += packet + b'\xff\xff\x00\x00\x00\x00\x00'
            for PlayerSocket in range(self.player.ClientDict["ClientCounts"]):
                self.player.ClientDict["Clients"][str(low_id)]["SocketInfo"].send(self.buffer)
                break
        except:
            pass

        if packet_settings["ShowPacketsInLog"] == True:
            print(self.id, self.__class__.__name__)

    def writeVint(self, data, rotate: bool = True):
        final = b''
        if data == 0:
            self.writeByte(0)
        else:
            data = (data << 1) ^ (data >> 31)
            while data:
                b = data & 0x7f

                if data >= 0x80:
                    b |= 0x80
                if rotate:
                    rotate = False
                    lsb = b & 0x1
                    msb = (b & 0x80) >> 7
                    b >>= 1
                    b = b & ~0xC0
                    b = b | (msb << 7) | (lsb << 6)

                final += b.to_bytes(1, 'big')
                data >>= 7
        self.buffer += final

    def writeString(self, string: str = None):
        if string is None:
            self.writeInt((2 ** 32) - 1)
        else:
            encoded = string.encode('utf-8')
            self.writeInt(len(encoded))
            self.buffer += encoded

    def write_string_reference(self, string: str = None):

        encoded = string.encode('utf-8')
        self.writeInt16(0)
        self.writeVint(len(encoded))
        self.buffer += encoded

    def writeByte(self, data):
        self.writeInt(data, 1)

    def writeInt16(self, data):
        self.writeInt(data, 2)

    def writeScId(self, x, y):
        self.writeVint(x)
        self.writeVint(y)