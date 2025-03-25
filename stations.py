from station import Station
from datafile import DataFile

class Stations:
	def __init__(self):
		self.stations = []
		self.stationFile = DataFile("stations.txt")
		self.loadStations()

	def loadStations(self):
		self.stations.append(Station(1,"Overhead By Upper Pig Barn",1,.2,"2010",18))
		self.stations.append(Station(2,"Overhead By Vivax Aureocaulis",1,.2,"2010",18))
		self.stations.append(Station(2,"Overhead By Original Pond",2,1,"2010",18))
		print(self.stationFile.readFile())
		
	def getStations(self):
		return self.stations
