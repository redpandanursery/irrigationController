from station import Station
from datafile import DataFile

class Stations:
	def __init__(self):
		self.stations = []
		self.stationFile = DataFile("stations.txt")
		self.loadStations()

	def loadStations(self):
		self.stations.append(Station(1,"Upper Pig Barn",1,30,"2010",18))
		print(self.stationFile.readFile())
		
	def getStations(self):
		return self.stations
