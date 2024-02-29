
from numpy import mod
#from assets.voidapex11.AboutMe import *
from assets.voidapex11.clear import *
from assets.voidapex11.logging import *
import math
import statistics
from cmath import *
from math import *

doClear = False

import cmath


class Calc:
  
  import random
  import os
  import sys
  try:
    import numpy as np
  except:
    import subprocess
    completed_process = subprocess.run("pip install numpy", shell=True)
    del subprocess
    import numpy as np

  import re
  import numpy as np
  

  operators = ['+', '-', '*', '/', '**', '%', '//']

  alowed = [
      '.', '+', '-', '*', '/', '**', '^', '//', '%', '0', '1', '2', '3', '4',
      '5', '6', '7', '8', '9', '-', '#'
  ]  # Include the minus sign for negative numbers
  d = 0
  

  def replace_functions(self, data: list):
    '''
    this trys to run each inputed item as a math., cmath., self.np., and statistics. function 
    '''
    nd = []
    mtypes = ['math.', 'cmath.', 'self.np.', 'statistics.']
    breaky = False
    logging.debug(f'data inputed into replace_functions is {data}')
    for i in data:
      if breaky: break
      for a in mtypes:
        if breaky: break
        try:
          if breaky: break
          tmp = a + i
          if float(eval(tmp)):
            nd.append(a + i)
            breaky = True
            if breaky: break
        except:
          pass
      if self.isInt(i) or self.isFloat(i) or i in self.operators:
        nd.append(i)
      if breaky: break
    logging.debug(f'in replaced functions after filtering is\n {nd}')
    return nd


  def intro(self):
    '''
    intro prints a guide to how to use the calculatar
    '''
    print('''    Welcome to the calculatarla

  we use all of the python operators and have float compatability
  however numbers and operators must all be seperated by a space

  for example:
  1 + 1  NOT  1+1

  use clear to clear the console, quit to exit and help to display this mesage
  these comands must be all lower case 
  e.g. clear not Clear or CLEAR or _clear or \' clear\'

  +	Addition	        1 + 1 = 2	
  -	Subtraction	      3 - 2	= 1
  *	Multiplication	  2 * 3	= 6
  /	Division	        6 / 3 = 2	
  %	Modulus	          5 % 2	= 1
  **	Power          	3 ** 2 = 9	
  //	Floor division	15 // 2 = 7

  press enter to hide this message
  ''')


  def terminate(self):
    '''
    this calls the clear function then ends the program
    '''
    clear()
    self.sys.exit()


  def isInt(self, intAble: str):
    '''
    It trys to convert a input into a int
    if this fails it returns false
    otherwise it returns True
    '''
    try:
      int(intAble)
      return True
    except ValueError:
      return False


  def isFloat(self, floatAble: str):
    '''
    It trys to convert a input into a float
    if this fails it returns false
    otherwise it returns True
    '''
    try:
      float(floatAble)
      return True
    except:
      return False


  def isStr(self, strAble: str):
    '''
    It trys to convert a input into a string
    if this fails it returns false
    otherwise it returns True
    '''
    try:
      str(strAble)
      return True
    except:
      return False
    
  
  def listify(self, data: str):
    '''
    this trys to convert the input into a valid list for mathIt
    '''
    logging.debug('data inputed into listify is ' + data)
    lst = []
    temp = ''
    modey = False
    for i in data:
      if modey == (i in self.alowed):
        temp += i
      else:
        if temp != '':
          lst.append(temp)
          temp = ''  # Reset temp after adding to the list
        temp = i
        modey = not modey
    if temp != '':
      lst.append(temp)
    return lst

  
  def mathIt(self, data):
    '''
    MathIt filters out invalid inputs so that all that remains is a valid str
    so it converts \"2 + badData 2\" to \"2+2\"
    this makes the calculatar safe and reliable
    '''
    data = self.listify(data)
    logging.debug(f'data returned from sistify is {data}')
    data = self.replace_functions(data)
    logging.debug(self.alowed)
    # handle negative numbers
    i = 0
    while i < len(data):
      if data[i] == '-':
        if i + 1 < len(data) and (self.isInt(data[i + 1])
                                  or self.isFloat(data[i + 1])):
          data[i] = data[i] + data[
              i + 1]  # Combine the minus sign and the following number
          data[i + 1] = None  # Set the next item to None
        else:
          data[i] = 0 - int(
              data[i + 2])  # Convert the negative number to a negative integer
          data[i + 1] = None  # Set the next item to None
          data[i + 2] = None  # Set the next-next item to None
      i += 1
    logging.debug('data after being with while loop is ' + str(data))

    data = [x for x in data
            if x is not None]  # Remove the None values from the list

    logging.debug(f'data after none is removed is {data}')
    #replace ^ with **
    data = [i.replace('^', '**') for i in data]
    data = [i.replace('?', 'last') for i in data]
    # handle division by zero
    if '/' in data:
      divisor_index = data.index('/')
      if data[divisor_index +
              1] == 0 or data[divisor_index +
                              1] == '0':  # Check if the denominator is zero
        print('Error: Division by zero')
        return
    logging.debug(f'data after various filters and swichouts is {data}')
    # handle floats
    for x in range(len(data)):
      if self.isFloat(data[x]) and not self.isInt(data[x]):
        data[x] = float(data[x])
    logging.debug('data after floats are handled is ' + str(data))
    # handle floats
    for q in range(len(data)):
      if self.isFloat(data[q]) and not self.isInt(data[q]):
        data[q] = int(float(data[q]))

    final = ''
    for i in data:
      final += str(i)

    for k in range((len(data) + 1) * 2):
      final = final.rstrip('+-*/%')  # Remove all operators found on the end
    logging.debug('final is ' + str(final))

    if final == '2+2':
      print(5)
      return
    else:
      exec(f'print({final})')


  def start(self):
    '''
    Starts the Calculatar
    '''
    last = 0
    self.intro()
    input()
    clear()
    stage = 0
    while True:
      stage += 1
      #stop console being 20 million lines long
      if stage == 20:
        print('do you want to clear the console')
        print('y/n')
        ans = input().lower().startswith('y')
        if ans:
          stage = 0
          clear()
          pass
        else:
          stage = 15
          pass
      text = input(' >> ')
      if text.lower() == 'exit':
        self.terminate()
      if text.lower() == 'clear':
        stage = 0
        clear()
        pass
      if text.lower() == 'help':
        self.intro()
        pass

      try:
        nstext = ''
        for i in text:
          if i != ' ':
            nstext += i
        self.mathIt(nstext)
      except Exception as e:
        print(
            'there was an uncaught error in the mathsIt function, we apologise for the inconvenience'
        )
        print(f'the error was: {e}')
        raise e
        pass


calc = Calc()
#Calc.start()
