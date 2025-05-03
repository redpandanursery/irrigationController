import time
import threading
from controller import Controller
from display import Display
import tkinter as tk

loopCount = 0

def runController():
  global systemController
  global systemDisplay
  #systemController = Controller()
  systemDisplay.createDisplay()
  loopControl()

def loopControl():
  global systemController
  global systemDisplay
  global loopCount

  loopCount = loopCount+1
  if loopCount % 6 == 0:
    systemController.stations.updateStations()

  systemController.systemLoop()
  systemDisplay.updateDisplay()
  timer = threading.Timer(10,loopControl)
  timer.start()

systemController = Controller()

root = tk.Tk()
systemDisplay = Display(root,systemController)

root.geometry("500x500")
root.title("Irrigation Controller")

root.after(100,runController)
root.mainloop()




