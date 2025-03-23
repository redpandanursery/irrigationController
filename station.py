class Station:
	def __init__(self,pin,name,pipeZone,runTime,lastRun,runAfter):
		self.pin = pin
		self.name = name
		self.pipeZone = pipeZone
		self.runTime = runTime
		self.lastRun = lastRun
		self.runAfter = runAfter
		
	def runStation(self):
		print("run station ")
	
	def isTimeToRunNow(self):
		return True
		
	def getZone(self):
		return self.zone
		
	def getRunTime(self):
		return self.runTime
