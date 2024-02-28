import time

def scroll(str, t):
  '''
  scroll(str string, t float or int) -> None
  prints every character of str with a delay of t
  '''
  for x in str:
    print(x, end="", flush=True)
    time.sleep(t)
  print()