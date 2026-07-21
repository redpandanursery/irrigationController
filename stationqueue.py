from datetime import datetime
import tkinter as tk
import copy

class StationQueue:
	def __init__(self,pump):
		self.stationsInQueue = []
		self.stationsToRepeat = []
		self.pump = pump
		self.pumpRequired = False

	def doStationsNeedPumpOn(self):
		return self.pumpRequired

	def getRunningDisplay(self):
		content = ""
		for station in self.stationsInQueue:
			
			if (station['running']):
				content = content + station['stationObj'].getName() + " \n"
		return content
	
	def getQueuedDisplay(self):
		content = ""
		for station in self.stationsInQueue:
			if (station['running'] == False):
				content = content + station['stationObj'].getName() + "\n"
		return content

	def addStation(self,stationObj,runTime=""):
		if (runTime != ""):
			calculatedRunTime = float(runTime)
		else:
			calculatedRunTime = stationObj.getRunTime()

		if ((calculatedRunTime / stationObj.getRunTime()) > .6):
			stationObj.saveRunTime()

		runObj = {"stationObj":stationObj,"runTime":calculatedRunTime,"startTime":False,"running":False}
		self.stationsInQueue.append(runObj)
		if (stationObj.getRepeat() > 0):
			self.stationsToRepeat.append({"repeat":stationObj.getRepeat(),"runObj":runObj})
		#self.runStation(runObj)

	def lookToAddRepeat(self):
		newStationsToRepeat = []
		if (len(self.stationsToRepeat) > 0):
			for repeatStation in self.stationsToRepeat:
				self.stationsInQueue.append(copy.copy(repeatStation["runObj"]))
				remainingRepeats = repeatStation["repeat"] - 1
				if (remainingRepeats > 0):
					newStationsToRepeat.append({"repeat":remainingRepeats,"runObj":repeatStation["runObj"]})
			self.stationsToRepeat = newStationsToRepeat

	def runStation(self,stationObj):
		if (self.pump.isCharged() == False and stationObj["stationObj"].getUsesPump()):
			stationObj["runTime"] = stationObj["runTime"] + self.pump.getChargeTime()
		stationObj["running"] = True
		stationObj["startTime"] = datetime.now()
		stationObj["stationObj"].runStation()

	def stopStation(self,stationObj):
		stationObj["running"] = False
		stationObj["stationObj"].stopStation()

	def loop(self):
		self.lookToAddRepeat()
		stationsDoneQnty = self.lookForStationsThatAreDone() #returns qnty of stations turned off
		stationsRunningQnty = self.lookForStationsToRun() #returns gpm qnty of stations running

		if (stationsDoneQnty > 0 and stationsRunningQnty == 0):
			self.pump.turnOff() #only turn off the pump if stations were running and ended this cycle, otherwise it will turn off the pump when running manually
		
		if (self.pump.getIsOn() == False and stationsRunningQnty > 0):
			if (self.pumpRequired == True):
				self.pump.turnOn(stationsRunningQnty)

		self.pump.setUsage(stationsRunningQnty)

	def lookForStationsThatAreDone(self):
		#stop stations that are done
		stationsTurnedOff = 0
		for station in self.stationsInQueue:
			if (station["running"] == True):
				totalRunTime = datetime.now() - station["startTime"]
				runTimeInMinutes = totalRunTime.total_seconds()/60
				if (runTimeInMinutes >= station["runTime"]):
					self.stopStation(station)
					stationsTurnedOff += 1

		#remove stations that are done from the queue list
		newStationList = []
		removingAnyFromQueue = False
		for station in self.stationsInQueue:
			if (station['startTime'] != False and station['running'] == False):
				removingAnyFromQueue = True #keep this here for later use
			else:
				newStationList.append(station)
		self.stationsInQueue = newStationList
		return stationsTurnedOff

	def lookForStationsToRun(self):	
		capacityTracker = {
			"pipeZone1" : {
				"capacity" : 40,
				"running" : 0
			},
			"pipeZone2" : {
				"capacity" : 20,
				"running" : 0
			},
			"pipeZone3" : {
				"capacity" : 12,
				"running" : 0
			}
		}

		#reset running count for each zone
		capacityTracker["pipeZone1"]["running"] = 0
		capacityTracker["pipeZone2"]["running"] = 0
		capacityTracker["pipeZone3"]["running"] = 0
		isPumpRequired = False

		#get existing zone usage
		runningPins = []
		for station in self.stationsInQueue:
			if (station["running"] == True):
				runningPins.append(int(station["stationObj"].getPin()))
				if (station["stationObj"].getUsesPump() == True):
					isPumpRequired = True

				capacityTracker["pipeZone"+str(station["stationObj"].getZone())]["running"] += station["stationObj"].getUsage()
		
		#run stations if there is room
		#print(runningPins)
		for station in self.stationsInQueue:
			if (station["running"] == False):
				#only run if not already running
				#print(station["stationObj"].getPin() + " not in ")
				#print(runningPins)
				#print(int(station["stationObj"].getPin()) not in runningPins)
				if (int(station["stationObj"].getPin()) not in runningPins):
					zoneReference = "pipeZone"+str(station["stationObj"].getZone())
					gpm = station["stationObj"].getUsage()
					zoneRemainingCapacity = capacityTracker[zoneReference]["capacity"] - capacityTracker[zoneReference]["running"]
					if (gpm <= zoneRemainingCapacity):
						existingPumpCapacity = capacityTracker["pipeZone1"]["running"] + capacityTracker["pipeZone2"]["running"] + capacityTracker["pipeZone3"]["running"]
						if ((existingPumpCapacity + gpm) <= self.pump.getGpmCapacity()):
							runningPins.append(int(station["stationObj"].getPin()))
							self.runStation(station)
							capacityTracker[zoneReference]["running"] += gpm
							if (station["stationObj"].getUsesPump() == True):
								isPumpRequired = True
						

		#run the pump controls
		totalCapacityRequired = capacityTracker["pipeZone1"]["running"] + capacityTracker["pipeZone2"]["running"] + capacityTracker["pipeZone3"]["running"]
		self.pumpRequired = isPumpRequired

		return totalCapacityRequired