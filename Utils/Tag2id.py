# -*- coding: utf-8 -*-
import sys

def getId(Hashtag):
	TagChar = ("0", "2", "8", "9", "P", "Y", "L", "Q", "G", "R", "J", "C", "U", "V")
	if not Hashtag.startswith('#'):
		print('Wrong Hashtag')
		return


	TagArray = list(Hashtag[1:].upper())
	Id = 0
	for i in range(len(TagArray)):
		Character = TagArray[i]
		try:
			CharIndex = TagChar.index(Character)
		except ValueError:
			print('Wrong Hashtag : should only contain "0", "2", "8", "9", "P", "Y", "L", "Q", "G", "R", "J", "C", "U" or "V"')
			sys.exit()
		Id *= len(TagChar)
		Id += CharIndex

	return Id



def getHLid(Hashtag):
	TagChar = ("0", "2", "8", "9", "P", "Y", "L", "Q", "G", "R", "J", "C", "U", "V")
	if not Hashtag.startswith('#'):
		print('Wrong Hashtag')
		return


	TagArray = list(Hashtag[1:].upper())
	Id = 0
	for i in range(len(TagArray)):
		Character = TagArray[i]
		try:
			CharIndex = TagChar.index(Character)
		except ValueError:
			print('Wrong Hashtag : should only contain "0", "2", "8", "9", "P", "Y", "L", "Q", "G", "R", "J", "C", "U" or "V"')
			sys.exit()
		Id *= len(TagChar)
		Id += CharIndex

	HighLow = []
	HighLow.append(Id % 256)
	HighLow.append((Id - HighLow[0]) >> 8)


	return HighLow

if __name__ == '__main__':
	
	Hashtag = str(input('Enter your hashtag \n>>'))
	if not Hashtag.startswith('#'):
		print('Wrong Hashtag')
		sys.exit()
	HlId = getHLid(Hashtag)
	ID = getId(Hashtag)
	print('Id = {}'.format(ID))
	print('HighLowId = {}-{}'.format(HlId[0],HlId[1]))