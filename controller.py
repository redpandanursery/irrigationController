import time
from pump import Pump
from stations import Stations
from board import Board
from stationqueue import StationQueue

class Controller:
	def __init__(self):
		self.testN = 0 ;
		self.board = Board()
		self.pump = Pump(2,1)
		self.stations = Stations()
		self.queued = StationQueue(self.pump)

	def getPumpObj(self):
		return self.pump
		
	def test(self):
		self.pump.turnOn()
		time.sleep(2)
		self.pump.turnOff()
		
	def checkForStationsToRun(self):
		for station in self.stations.getStations():
			if (station.isTimeToRunNow()):
				self.queued.addStation(station)
		"""
		if (self.testN == 0):
			self.queued.addStation(self.stations.getStations()[0])
			self.queued.addStation(self.stations.getStations()[1])
			self.queued.addStation(self.stations.getStations()[2])
		self.testN+=1
		"""

	def systemLoop(self):
		print("controller loop")
		self.checkForStationsToRun()
		self.queued.loop()
		#time.sleep(10)
		#timer = threading.Timer(10,self.systemLoop)
