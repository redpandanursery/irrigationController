from station import Station

class Stations:
	def __init__(self):
		self.stations = []
		self.loadStations()
		
	def loadStations(self):
		self.stations.append(Station(1,"Upper Pig Barn",1,30,"2010",18))
		
	def getStations(self):
		return self.stations
