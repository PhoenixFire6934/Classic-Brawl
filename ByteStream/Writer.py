from Utils.Helpers import Helpers

class Writer:
    def __init__(self, client, endian: str = 'big'):
        self.client = client
        self.endian = endian
        self.buffer = b''

    def writeInt(self, data, length = 4):
        self.buffer += data.to_bytes(length, self.endian, signed=True)

    def writeUInteger(self, integer: int, length: int = 1):
        self.buffer += integer.to_bytes(length, self.endian, signed=False)

    def writeLong(self, data):
        self.writeInt(data, 8)

    def writeLogicLong(self, data):
        self.writeVInt(0)
        self.writeVInt(data)

    def writeArrayVint(self, data):
        self.writeVInt(len(data))
        for x in data:
            self.writeVInt(x)

    def writeUInt8(self, integer: int):
        self.writeUInteger(integer)

    def writeInt8(self, integer: int):
        self.writeInt(integer, 1)

    def writeInt16(self, data):
        self.writeInt(data, 2)

    def writeBool(self, boolean: bool):
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
        print(f'{Helpers.yellow}[SERVER] PacketID: {self.id}, Name: {type(self).__name__}, Length: {len(self.buffer)}')


    def sendByID(self, ID):
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
            Helpers.connected_clients["Clients"][str(ID)]["SocketInfo"].send(self.buffer)
        except:
            pass

    def writeVInt(self, data, rotate: bool = True):
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

    def writeDataReference(self, x, y=0):
        if x != 0:
            self.writeVInt(x)
            self.writeVInt(y)
        else:
            self.writeVInt(0)


    def writeString(self, string: str = None):
        if string is None:
            self.writeInt(-1)
        else:
            encoded = string.encode('utf-8')
            self.writeInt(len(encoded))
            self.buffer += encoded

    def writeStringShort(self, string: str = None):
        if string is None:
            self.writeInt(-1)
        else:
            encoded = string.encode('utf-8')
            self.writeInt8(len(encoded))
            self.buffer += encoded

    def writeStringReference(self, string: str = None):
        encoded = string.encode('utf-8')
        self.writeInt16(0)
        self.writeVInt(len(encoded))
        self.buffer += encoded

    def writeByte(self, data):
        self.writeInt(data, 1)

    def writeNullVInt(self):
        self.writeVInt(-1)

    def size(self):
        return len(self.buffer)

    def getRaw(self):
        return self.buffer

    def writeBytes(self, data):
        self.buffer += data

    writeBoolean = writeBool
    writeInt32   = writeInt