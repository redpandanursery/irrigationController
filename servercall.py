import requests
import json
from datafile import DataFile

class ServerCall:
  def __init__(self,method,systemController):
    self.systemController = systemController

    self.headers = {"User-Agent": "XY","Accept": "*/*"}

    if (method == "getserverdata"):
      self.getServerData()

  def getServerData(self):
    status = "success"
    url = 'https://redpandanursery.com/controller/index.php?page=api&method=readdata'
    lastrun = DataFile("lastrun.txt")
    try:
      response = requests.post(url,data ={'lastrun':lastrun.readFile()},headers=self.headers)
      if (response.status_code == 200):
        jsonResponse = json.loads(response.text)
        if (jsonResponse['status'] == "ok"):
          #update station data
          file = DataFile("stations.txt")
          file.writeFile(json.dumps(jsonResponse['stations']))
          self.systemController.stations.updateStations()

          #run manual stations
          for manualStation in jsonResponse['queue']:
            self.systemController.runStationOnPin(manualStation['pinNumber'],manualStation['runTime'])
        else:
          status = "not json"
    except:
      status = "fail"
      