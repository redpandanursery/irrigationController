class Pump:
	def __init__(self,board):
		#self.stationCapacity = stationCapacity
		self.pinNumber = 0
		self.isOn = False
		self.gpm = 12
		self.gpmUsage = 0
		self.board = board
		self.pinPosition = 0 #for testing pin numbers
		self.chargeTime = 7

	def setPump(self,pumpSize):
		switchWhileRunning = False
		if (self.isOn == True):
			switchWhileRunning = True
			self.turnOff()
		
		if (pumpSize == "smallpump"):
			self.pinNumber = 0
			self.gpm = 12
			self.chargeTime = 7

		if (pumpSize == "mediumpump"):
			self.pinNumber = 1
			self.gpm = 16
			self.chargeTime = 3
		
		if (pumpSize == "bigpump"):
			self.pinNumber = 1
			self.gpm = 25
			self.chargeTime = 3

		if (switchWhileRunning == True):
			self.turnOn()
	
	def setUsage(self,gpm):
		self.gpmUsage = gpm

	def getGpmCapacity(self):
		return self.gpm
	
	def getGpmUsage(self):
		return self.gpmUsage
	
	def togglePins(self):
		pins = [26,19,13,6,5,0,21,20,16,12,1,7,8,25,24,23] #remaining 5 16 12 7 8
		if (self.pinPosition > 0):
			self.board.setPin(pins[self.pinPosition-1],"LOW")
		self.board.setPin(pins[self.pinPosition],"HIGH")
		print("Test Pin:")
		print(pins[self.pinPosition])
		self.pinPosition = self.pinPosition+1

		
	def isCharged(self):
		return self.isOn
	
	def getChargeTime(self):
		return self.chargeTime
		
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

