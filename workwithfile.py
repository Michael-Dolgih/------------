massive = open('games.txt', encoding= 'utf-8').read().splitlines()
def index():
  global massvie
  for e in massive:
    print(e)

def find(id):
  global massive
  for i in range(0, len(massive)):
    if i == id:
      print(massive[i-1])

def where(pattern):
  global massive
  for e in massive:
    if pattern in e.lower():
      print(e)


  
  
inputs = input()
if inputs == 'index':
  index()
elif inputs == 'find':
  print('vvedi nomer stroki')
  id = int(input())
  find(id)
elif inputs == 'where':
  print('vvedi slovo')
  pattern = input()
  where(pattern)
else:
  print('nothing')
