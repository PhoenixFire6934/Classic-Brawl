from io import BufferedReader, BytesIO


class Reader(BufferedReader):
    def __init__(self, initial_bytes, endian: str = 'big'):
        super().__init__(BytesIO(initial_bytes))
        self.buffer = initial_bytes
        self.endian = endian
        self.i = 0

    def readByte(self):
        return int.from_bytes(self.read(1), "big")

    def readVInt(self):
        n = self._read_varint(True)
        return (n >> 1) ^ (-(n & 1))

    def readShort(self, length=2):
        return int.from_bytes(self.read(length), "big")

    def readInt(self, length=4):
        return int.from_bytes(self.read(length), "big")

    def readLong(self):
        return self.readInt(8)

    def readUInt8(self) -> int:
        return self.readUInteger()

    def readUInteger(self, length: int = 1) -> int:
        result = 0
        for x in range(length):
            byte = self.buffer[self.i]

            bit_padding = x * 8
            if self.endian == 'big':
                bit_padding = (8 * (length - 1)) - bit_padding

            result |= byte << bit_padding
            self.i += 1

        return result

    def _read_varint(self, rotate: bool = True):
        result = 0
        shift = 0
        while True:
            byte = self.readByte()
            if rotate and shift == 0:
                seventh = (byte & 0x40) >> 6
                msb = (byte & 0x80) >> 7
                n = byte << 1
                n = n & ~0x181
                byte = n | (msb << 7) | seventh
            result |= (byte & 0x7f) << shift
            shift += 7
            if not (byte & 0x80):
                break
        return result


    def readBool(self) -> bool:
        if self.readUInt8() >= 1:
            return True
        else:
            return False

    def readDataReference(self):
        a = self.readVInt()
        if a != 0:
            b = self.readVInt()
        else:
            b = -1
        return a, b

    def readString(self):
        length = self.readInt()
        if length == pow(2, 32) - 1:
            return b""
        else:
            try:
                decoded = self.read(length)
            except MemoryError:
                raise IndexError("String out of range!")
            else:
                return decoded.decode('utf-8')

    def peekInt(self, length=4):
        return int.from_bytes(self.peek(length)[:length], "big")

    def readLogicLong(self):
        x = self.readVInt()
        y = self.readVInt()
        return x, y