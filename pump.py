class Pump:
	def __init__(self,stationCapacity,pinNumber):
		self.stationCapacity = stationCapacity
		self.pinNumber = pinNumber
		self.isOn = False
		self.gpm = 50
		self.gpmUsage = 0

	def setUsage(self,gpm):
		self.gpmUsage = gpm

	def getGpmCapacity(self):
		return self.gpm
	
	def getGpmUsage(self):
		return self.gpmUsage
		
	def turnOn(self,gpmUsage):
		print("turn pump on")
		self.isOn = True
		self.gpmUsage = gpmUsage
		
	def turnOff(self):
		print ("turn pump off")
		self.isOn = False
		self.gpmUsage = 0

	def getIsOn(self):
		return self.isOn

