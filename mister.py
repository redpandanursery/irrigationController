import threading
from datetime import datetime
import time

class Mister():
  def __init__(self,board):
    self.sunRise = 6
    self.sunSet = 21
    self.runAtNight = False
    self.board = board
    self.pin = 27
    self.mistSeconds = 10
    self.defaultInterval = 10
    timer = threading.Timer(20,self.loop)
    timer.start()

  def getInterval(self):
    interval = self.defaultInterval

    current_hour = self.getHour()
    
    if (current_hour < 8):
      interval = interval * 3
    elif (current_hour < 10):
      interval = interval * 2
    elif (current_hour > 20):
      interval = interval * 2
    
    return interval
  
  def getHour(self):
    now = datetime.now()
    return now.hour
  
  def loop(self):
    hour = self.getHour()
    if (self.runAtNight == True or (hour >= self.sunRise and hour <= self.sunSet)):
      self.board.setPin(self.pin,"HIGH")
      print("mist")
      time.sleep(self.mistSeconds)
      self.board.setPin(self.pin,"LOW")

    timer = threading.Timer(self.getInterval()*60,self.loop)
    timer.start()