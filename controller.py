import time
from pump import Pump
from stations import Stations
from board import Board
from queue import Queue

class Controller:
	def __init__(self):
		self.board = Board()
		self.pump = Pump(2,1)
		self.stations = Stations()
		self.queue = Queue()
		self.checkForStationsToRun()
		
	def test(self):
		self.pump.turnOn()
		time.sleep(2)
		self.pump.turnOff()
		
	def checkForStationsToRun(self):
		self.queue.addStation(self.stations.getStations()[0])
