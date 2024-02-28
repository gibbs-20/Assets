import os
import json

from Assets.voidapex11.setting import *
settings['doClear'] = setting('doClear', defaltData=True)

def togle_DoClear():
  settings1 = {'doClear': not data['doClear']}
  try:
    with open("assets/appData.json", "w+") as file:
      try:
        tf = json.load(file)
        tf['doClear'] = not tf['doClear']
        json.dump(tf, file, indent=2)
      except:
        tf = {}
        tf['doClear'] = settings1['doClear']
        json.dump(tf, file, indent=2)
  except:
    with open("assets/appData.json", "x") as file:
      json.dump(settings1, file, indent= 2)

def clear():
  if settings['doClear']:
    os.system("clear")