class Pump:
	def __init__(self,stationCapacity,pinNumber,board):
		self.stationCapacity = stationCapacity
		self.pinNumber = pinNumber
		self.isOn = False
		self.gpm = 50
		self.gpmUsage = 0
		self.board = board

	def setUsage(self,gpm):
		self.gpmUsage = gpm

	def getGpmCapacity(self):
		return self.gpm
	
	def getGpmUsage(self):
		return self.gpmUsage
		
	def turnOn(self,gpmUsage):
		self.board.setPin(self.pinNumber,"HIGH")
		self.isOn = True
		self.gpmUsage = gpmUsage
		
	def turnOff(self):
		self.board.setPin(self.pinNumber,"LOW")
		self.isOn = False
		self.gpmUsage = 0

	def getIsOn(self):
		return self.isOn

