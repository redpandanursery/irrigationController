from datetime import datetime
from datafile import DataFile
import json

class Station:
	def __init__(self,stationData,board):
		self.board = board
		self.runAfter = 48 #default run after time if not provided
		self.fields = ["pin","name","pipeZone","runTime","lastRun","runAfter","gpm","usesPump"]
		self.processStationData(stationData)

	def getRunAfter(self):
		return float(self.runAfter)

	def processStationData(self,stationData):
		for field in self.fields:
			if field in stationData:
				setattr(self,field,stationData[field])
		
	def getName(self):
		return self.name
	
	def runStation(self):
		self.board.setPin(self.pin,"HIGH")

	def stopStation(self):
		self.board.setPin(self.pin,"LOW")

	def saveRunTime(self):
		currentRunTime = datetime.now()
		lastRunFileObj = DataFile("lastrun.txt")
		lastRunJSON = json.loads(lastRunFileObj.readFile())
		lastRunJSON[str(self.pin)] = currentRunTime.strftime("%Y-%m-%d %H:%M:%S")
		lastRunFileObj.writeFile(json.dumps(lastRunJSON))

	def getLastRunTime(self):
		lastRunFileObj = DataFile("lastrun.txt")
		lastRunJSON = json.loads(lastRunFileObj.readFile())
		if str(self.pin) in lastRunJSON:
			timeString = lastRunJSON[str(self.pin)]
		else:
			timeString = "2025-01-01 00:00:00"
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
	
	def getPin(self):
		return self.pin
		
	def getZone(self):
		return self.pipeZone
		
	def getRunTime(self):
		return float(self.runTime)
	
	def getUsage(self):
		return float(self.gpm)
