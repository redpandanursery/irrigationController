class StationQueue:
	def __init__(self):
		self.stationsInQueue = []

	def addStation(self,stationObj):
		runObj = {"stationObj":stationObj,"runTime":stationObj.getRunTime(),"running":False}
		self.stationsInQueue.append(runObj)
		print("added station ")
		
	def runStation(self,stationObj):
		stationObj.running=True
