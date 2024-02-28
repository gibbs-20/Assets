import os
import json

settings = {
  'doClear': True
}


try:
  with open("assets/appData.json", "r+") as file:
    try:
      tf = json.load(file)
    except:
      tf = {}
    try: 
      if tf['doClear']:
        settings = tf
    except:
      tf['doClear'] = True
      json.dump(tf, file)
except:
  with open("assets/appData.json", "x") as file:
    json.dump(settings, file, indent= 2)

with open("assets/appData.json", "r") as read_file:
  data = json.load(read_file)

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