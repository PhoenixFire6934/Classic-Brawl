# -*- coding: utf-8 -*-
import math

def getIdFromHl():
	High = int(input('>>'))
	Low = int(input('>>'))
	return (Low << 8) + High


def getHashtagfromId(Id = None):
	if not Id:
		Id = getIdFromHl()

	TagChar = ("0", "2", "8", "9", "P", "Y", "L", "Q", "G", "R", "J", "C", "U", "V")
	Tag = []
	while Id > 0:
		CharIndex = math.floor(Id % len(TagChar))
		Tag.insert(0,TagChar[CharIndex])
		Id -= CharIndex
		Id /= len(TagChar)

	return ''.join(Tag)


if __name__ == '__main__':
	print('#' + getHashtagfromId())
		