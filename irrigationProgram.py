import time
from controller import Controller

x = "hello world"
print(x)

systemController = Controller()
systemController.test()

f = open("/home/redpandanursery/GitHubProjects/irrigationController/stationList.csv","a")
f.write("new content 4")
f.close()
