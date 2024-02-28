#keepy
import os
import threading
import random
import string
import time



exit(0)



options = [x for x in (string.ascii_letters + string.digits)]

class remove:
  count = 0

  def remove(self):

    for a in os.listdir():
      if a.endswith('.py'):
        if not open(a, 'r').readline(5).startswith('#keep'):
          print(a)
          try:
            os.remove(a)
          except:
            pass
          self.count += 1



  def __init__(self, threads=5):
    for i in range(threads-1):
      threading.Thread(target=self.remove).start()
    self.remove()
    print(f'Removed {self.count} files!!')
    exit(0)

def getName(length: int):

  ret = ''
  for i in range(length):
    ret += random.choice(options)
  return ret

print(f'{__file__}\n{time.asctime()}')


def run(name):
  os.system('python3 ' + name)

def __init__():
  with open(__file__, 'r') as me:
    mecon = me.read()
    mecon = mecon.removeprefix('#keepy')

    while True:
      rannum = getName(30)
      with open(f'{rannum}.py', 'w') as file:
        file.write(mecon)
        if random.randint(1,20) == 1:
          threading.Thread(target=run, args=(f'{rannum}.py',)).start()

#remove()
#__init__()