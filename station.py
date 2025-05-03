from datetime import datetime
from datafile import DataFile
import json

class Station:
	def __init__(self,stationData):
		self.runAfter = 48 #default run after time if not provided
		self.fields = ["pin","name","pipeZone","runTime","lastRun","runAfter","gpm"]
		self.processStationData(stationData)

	def getRunAfter(self):
		return float(self.runAfter)

	def processStationData(self,stationData):
		print("processing station data")
		for field in self.fields:
			if field in stationData:
				setattr(self,field,stationData[field])
		
	def getName(self):
		return self.name
	
	def runStation(self):
		print("run station "+self.name)

	def saveRunTime(self):
		currentRunTime = datetime.now()
		lastRunFileObj = DataFile("lastrun.txt")
		lastRunJSON = json.loads(lastRunFileObj.readFile())
		lastRunJSON[str(self.pin)] = currentRunTime.strftime("%Y-%m-%d %H:%M:%S")
		lastRunFileObj.writeFile(json.dumps(lastRunJSON))

	def getLastRunTime(self):
		lastRunFileObj = DataFile("lastrun.txt")
		lastRunJSON = json.loads(lastRunFileObj.readFile())
		timeString = lastRunJSON[str(self.pin)]
		return datetime.strptime(timeString, "%Y-%m-%d %H:%M:%S")
	
	def getHoursSinceLastRun(self):
		return datetime.now() - self.getLastRunTime()
	
	def getTimeUntilNextRun(self):
		duration = self.getHoursSinceLastRun()
		duration_in_h = round(duration.total_seconds() / 3600,3)

		return self.getRunAfter() - duration_in_h

	def isTimeToRunNow(self):
		duration = self.getHoursSinceLastRun()
		duration_in_h = round(duration.total_seconds() / 3600,3)
		return duration_in_h >= self.getRunAfter()
		
	def getZone(self):
		return self.pipeZone
		
	def getRunTime(self):
		return self.runTime
	
	def getUsage(self):
		return self.gpm
