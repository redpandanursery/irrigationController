class Queue:
	def __init__(self):
		self.stationsInQueue = []
		self.runCheck()
		
	def addStation(self,stationObj):
		runObj = {"stationObj":stationObj,"runTime":stationObj.getRunTime(),"running":False}
		self.stationsInQueue.append(runObj)
		print("added station ")
		
	def runCheck(self):
		print("test run check")
