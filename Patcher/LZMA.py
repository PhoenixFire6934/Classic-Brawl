import lzma
from hashlib import md5



def len_2_bytes(datalen, max_len=4):
    data = []
    while datalen > 0:
        item = datalen % 256
        datalen = int(datalen / 256)
        data.append(item)
    while len(data) < max_len:
        data.append(0)
    return data


def compress(data, max_len = 4):
    filters = [
        {
            "id": lzma.FILTER_LZMA1,
            "dict_size": 256 * 1024,
            "lc": 3,
            "lp": 0,
            "pb": 2,
            "mode": lzma.MODE_NORMAL
        },
    ]

    compressed_data = lzma.compress(data, format=lzma.FORMAT_ALONE, filters=filters)
    lzmadata = bytearray()

    for i in range(0, 5):
        lzmadata.append(compressed_data[i])

    data_size = len_2_bytes(len(data), max_len)

    for size in data_size:
        lzmadata.append(size)
    for i in range(13, len(compressed_data)):
        lzmadata.append(compressed_data[i])


    return lzmadata
