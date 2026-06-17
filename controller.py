import time
import json
from pump import Pump
from stations import Stations
from boardcontrol import BoardControl
from stationqueue import StationQueue
from mister import Mister
from datafile import DataFile

class Controller:
	def __init__(self):
		self.testN = 0 ;
		self.board = BoardControl()
		self.pumps = {"smallPump":Pump(12,0,self.board),"bigPump":Pump(25,1,self.board)}
		self.pump = self.pumps["smallPump"]
		self.stations = Stations(self.board)
		self.queued = StationQueue(self.pump)
		self.mister = Mister(self.board)
		self.settingsFile = DataFile('settings.txt')

	def getPumpObj(self):
		return self.pump
	
	def runStationOnPin(self,pin,runTime):
		station = self.stations.getStationOnPin(pin)
		self.queued.addStation(station,runTime)
		
	def test(self):
		print('system controller working')
		
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

	def readSettings(self):
		settings = json.loads(self.settingsFile.readFile())

	def systemLoop(self):
		self.readSettings()
		self.checkForStationsToRun()
		self.queued.loop()
		#time.sleep(10)
		#timer = threading.Timer(10,self.systemLoop)
