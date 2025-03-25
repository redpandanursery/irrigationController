import time
import threading
from controller import Controller
import tkinter as tk

def runController():
  global systemController
  systemController = Controller()
  loopControl()

def loopControl():
  global systemController
  systemController.systemLoop()
  timer = threading.Timer(10,loopControl)
  timer.start()

systemController = False


root = tk.Tk()
root.geometry("500x500")
root.title("Irrigation Controller")
root.after(100,runController)
root.mainloop()

