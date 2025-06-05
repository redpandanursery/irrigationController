from station import Station
from datafile import DataFile
import json
from alert import Alert

class Stations:
	def __init__(self,board):
		self.board = board
		self.stations = []
		self.stationFile = DataFile("stations.txt")
		self.loadStations()
		self.updateStations()

	def getStationOnPin(self,pin):
		for stationObj in self.stations:
			if (stationObj.getPin() == pin):
				return stationObj
		

	def loadStations(self):
		stationText = self.stationFile.readFile()
		stationListObj = []
		try:
			stationListObj = json.loads(stationText)
		except:
			Alert('failed to load stations.txt from local file, no stations running')

		for station in stationListObj:
			self.stations.append(Station(stationListObj[station],self.board))

	def updateStations(self):
		try:
			stationText = self.stationFile.readFile()
			stationListObj = json.loads(stationText)
			for station in stationListObj:
				if ((int(station)-1) < len(self.stations)):
					self.stations[int(station)-1].processStationData(stationListObj[station])
				else:
					self.stations.append(Station(stationListObj[station]))
		except:
			print("error reading and updating station file")

	def getStations(self):
		return self.stations
