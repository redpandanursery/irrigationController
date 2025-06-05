import time
import threading
from controller import Controller
from display import Display
import tkinter as tk
from servercall import ServerCall

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

  try:
    loopCount = loopCount+1
    if loopCount % 180 == 0:
      call = ServerCall("getserverdata",systemController)
      loopCount = 1
    systemController.systemLoop()
    systemDisplay.updateDisplay()
  except:
    print("error occured")
      
  timer = threading.Timer(10,loopControl)
  timer.start()

systemController = Controller()

root = tk.Tk()
systemDisplay = Display(root,systemController)

root.geometry("500x600")
root.title("Irrigation Controller")

root.after(100,runController)
root.mainloop()




