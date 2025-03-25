from datetime import datetime

class StationQueue:
	def __init__(self):
		self.stationsInQueue = []

	def addStation(self,stationObj):
		runObj = {"stationObj":stationObj,"runTime":stationObj.getRunTime(),"startTime":False,"running":False}
		self.stationsInQueue.append(runObj)
		#self.runStation(runObj)
		
	def runStation(self,stationObj):
		stationObj["running"] = True
		stationObj["startTime"] = datetime.now()
		print("running station "+stationObj["stationObj"].getName())

	def stopStation(self,stationObj):
		stationObj["running"] = False
		print("stopping station "+stationObj["stationObj"].getName())

	def loop(self):
		self.lookForStationsThatAreDone()
		self.lookForStationsToRun()

	def lookForStationsThatAreDone(self):
		#stop stations that are done
		for station in self.stationsInQueue:
			if (station["running"] == True):
				totalRunTime = datetime.now() - station["startTime"]
				runTimeInMinutes = totalRunTime.total_seconds()/60
				if (runTimeInMinutes >= station["runTime"]):
					self.stopStation(station)

		#remove stations that are done from the queue list
		newStationList = []
		removingAnyFromQueue = False
		for station in self.stationsInQueue:
			if (station['startTime'] != False and station['running'] == False):
				removingAnyFromQueue = True #keep this here for later use
			else:
				newStationList.append(station)
		self.stationsInQueue = newStationList

	def lookForStationsToRun(self):
		capacityTracker = {
			"pipeZone1" : {
				"capacity" : 25,
				"running" : 0
			},
			"pipeZone2" : {
				"capacity" : 25,
				"running" : 0
			}
		}

		#reset running count for each zone
		capacityTracker["pipeZone1"]["running"] = 0
		capacityTracker["pipeZone2"]["running"] = 0

		#get existing zone usage
		for station in self.stationsInQueue:
			if (station["running"] == True):
				capacityTracker["pipeZone"+str(station["stationObj"].getZone())]["running"] += station["stationObj"].getUsage()

		#run stations if there is room
		for station in self.stationsInQueue:
			if (station["running"] == False):
				zoneReference = "pipeZone"+str(station["stationObj"].getZone())
				gpm = station["stationObj"].getUsage()
				zoneRemainingCapacity = capacityTracker[zoneReference]["capacity"] - capacityTracker[zoneReference]["running"]
				if (gpm <= zoneRemainingCapacity):
					self.runStation(station)
					capacityTracker[zoneReference]["running"] += gpm

		print("usage of zone 1: "+str(capacityTracker["pipeZone1"]["running"]))
		print("usage of zone 2: "+str(capacityTracker["pipeZone2"]["running"]))