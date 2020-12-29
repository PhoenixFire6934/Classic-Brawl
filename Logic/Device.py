class Device:
	AndroidID = None
	DeviveModel = None
	OpenUDID = None
	OSVersion = None
	isAndroid = False
	Language = None
	AllClient = []
	
	def __init__(self, socket):
		self.socket = socket
		
	def SendData(self, data):
		self.socket.send(data)