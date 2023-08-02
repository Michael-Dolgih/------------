massive = open('games.txt', encoding= 'utf-8').read().splitlines()
def index():
  global massvie
  return massive

def pretty_print(massive2):
  if type(massive2) == list:
    for i in massive2:
      print(i) 
  else:
    print(massive2)

def find(id):
  global massive
  for i in range(0, len(massive)):
    if i == id:
      return(massive[i-1])

def where(pattern):
  global massive
  result = []
  for e in massive:
    if pattern in e.lower():
      result.append(e)
  return(result)

def save():
  global massive 
  file = open('games.txt', 'w', encoding= 'utf-8')
  for e in massive:
    file.write(e+'\n')
  file.close

def update(id, text):
  global massive
  massive[id - 1] = text
  save()


inputs = ''
while inputs != 'exit':
    inputs = input()
    if inputs == 'index':
      pretty_print(index())
    elif inputs == 'find':
        pretty_print('vvedi nomer stroki')
        id = int(input())
        pretty_print(find(id))
    elif inputs == 'where':
        pretty_print('vvedi slovo')
        pattern = input()
        pretty_print(where(pattern))
    elif inputs == 'update':
        pretty_print('vvedi nomer stroki')
        id = int(input())
        pretty_print('vvedi text')
        text = input()
        pretty_print(update(id, text))

    else:
      pretty_print('nothing')
