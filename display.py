import tkinter as tk
from servercall import ServerCall


class Display:
  def __init__(self,root,systemController):
    self.root = root
    self.systemController = systemController

  def getPumpStateDisplay(self):
    onOrOff = self.systemController.getPumpObj().getIsOn()
    if (onOrOff):
      return "--- Running ---"
    else:
      return "<Off>"
    
  def getPumpUsage(self):
    usage = str(self.systemController.getPumpObj().getGpmUsage())
    capacity = str(self.systemController.getPumpObj().getGpmCapacity())
    return usage+"/"+capacity+"gpm"

  def togglePump(self):
    if (self.systemController.getPumpObj().getIsOn() == True):
      self.systemController.getPumpObj().turnOff()
    else:
      self.systemController.getPumpObj().turnOn(20)
    
    self.updateDisplay()

  def pullServerData(self):
    call = ServerCall("getserverdata",self.systemController)
  
  def createDisplay(self):
    self.pumpText = tk.Label(self.root,text="Pump Status:",font=('Arial',16))
    self.pumpText.pack(padx=10,pady=10)

    self.togglePumpButton = tk.Button(self.root, text="Turn Pump On/Off", command=self.togglePump)
    self.togglePumpButton.pack()

    self.pullDataButton = tk.Button(self.root, text="Pull Server Data", command=self.pullServerData)
    self.pullDataButton.pack()

    self.stationText = tk.Label(self.root,text="PH",font=('Arial',10))
    self.stationText.pack(padx=10,pady=10)

    self.stationListText = tk.Label(self.root,text="Station List",font=('Arial',10))
    self.stationListText.pack(padx=10,pady=10)


  def updateDisplay(self):
    self.pumpText.config(text="Pump Status: "+self.getPumpStateDisplay()+" "+self.getPumpUsage())
    runningStations = ""
    queuedStations = ""
    self.stationText.config(text="Running:\n"+self.systemController.queued.getRunningDisplay()+"\nQueued:\n"+self.systemController.queued.getQueuedDisplay())
    
    listText = ""
    for station in self.systemController.stations.getStations():
      listText = listText + "--"+station.getName()+"--" + "\n Runs in " + str(round(station.getTimeUntilNextRun(),2)) +" hours for "+str(station.getRunTime())+" minutes every "+str(station.getRunAfter())+" hours \n"
    self.stationListText.config(text="\nStations:\n"+listText)


