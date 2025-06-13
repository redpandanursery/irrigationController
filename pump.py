class Pump:
	def __init__(self,stationCapacity,pinNumber,board):
		self.stationCapacity = stationCapacity
		self.pinNumber = pinNumber
		self.isOn = False
		self.gpm = 50
		self.gpmUsage = 0
		self.board = board
		self.pinPosition = 0 #for testing pin numbers

	def setUsage(self,gpm):
		self.gpmUsage = gpm

	def getGpmCapacity(self):
		return self.gpm
	
	def getGpmUsage(self):
		return self.gpmUsage
	
	def togglePins(self):
		pins = [26,19,13,6,5,0,21,20,16,12,1,7,8,25,24,23]
		if (self.pinPosition > 0):
			self.board.setPin(pins[self.pinPosition-1],"LOW")
		self.board.setPin(pins[self.pinPosition],"HIGH")
		print("Test Pin:")
		print(pins[self.pinPosition])
		self.pinPosition = self.pinPosition+1

		

		
	def turnOn(self,gpmUsage):
		#self.togglePins()
		self.board.setPin(self.pinNumber,"HIGH")
		self.isOn = True
		self.gpmUsage = gpmUsage
		
	def turnOff(self):
		#self.togglePins()
		self.board.setPin(self.pinNumber,"LOW")
		self.isOn = False
		self.gpmUsage = 0

	def getIsOn(self):
		return self.isOn

