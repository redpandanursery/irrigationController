import time
from pump import Pump
from stations import Stations
from board import Board
from stationqueue import StationQueue

class Controller:
	def __init__(self):
		self.board = Board()
		self.pump = Pump(2,1)
		self.stations = Stations()
		self.queued = StationQueue()
		self.checkForStationsToRun()
		
	def test(self):
		self.pump.turnOn()
		time.sleep(2)
		self.pump.turnOff()
		
	def checkForStationsToRun(self):
		self.queued.addStation(self.stations.getStations()[0])
