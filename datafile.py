import os

class DataFile:
  def __init__(self,fileName):
    self.fileName = fileName
    self.piRootDirectory = "/home/redpandanursery/GitHubProjects/irrigationController/"
    if (os.path.isdir(self.piRootDirectory) == False):
      self.piRootDirectory = ""

  def readFile(self):
    f = open(self.piRootDirectory+self.fileName,"r")
    contents = f.read()
    f.close()
    return contents

  def writeFile(self,content):
    f = open(self.piRootDirectory+self.fileName,"w")
    f.write(content)
    f.close()
