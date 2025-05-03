from station import Station
from datafile import DataFile
import json

class Stations:
	def __init__(self):
		self.stations = []
		self.stationFile = DataFile("stations.txt")
		self.loadStations()
		self.updateStations()

	def loadStations(self):
		stationText = self.stationFile.readFile()
		stationListObj = json.loads(stationText)
		for station in stationListObj:
			self.stations.append(Station(stationListObj[station]))

	def updateStations(self):
		try:
			stationText = self.stationFile.readFile()
			stationListObj = json.loads(stationText)
			for station in stationListObj:
				self.stations[int(station)-1].processStationData(stationListObj[station])
		except:
			print("error reading and updating station file")

	def getStations(self):
		return self.stations
