massive = open('names.txt', encoding= 'utf-8').read().splitlines()
def index():
  global massvie
  return massive

def pretty_print(massive2):
  if type(massive2) == list:
    for l in range(0, len(massive2)):
      print(f'{l+1}) {massive2[l]}') 
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
  file = open('names.txt', 'w', encoding= 'utf-8')
  for i in range(len(massive)):
    massive[i]
    if i == len(massive)-1:
      file.write(massive[i])
    else:
      file.write(massive[i]+'\n')
  file.close

def update(id, text):
  global massive
  massive[id - 1] = text
  save()

def delete(id):
  global massive
  massive.pop(id - 1)
  save()

def create(name):
  global massive
  massive.append(name)
  save()
  
# def last_elem():
#    k = ['a', 'b', 'c', 'c', 'b']
#    for index in range(0, len(k)):
#      print(k[index])
#      if index == len(k)-1:
#         print('eto last')
#      else:
#        print('eto ne last')
#    print(len(k))
#    print(index)


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
    elif inputs == 'delete':
      pretty_print('vvedi nomer stroki')
      id = int(input())
      pretty_print(delete(id))
    elif inputs == 'create':
      pretty_print('vvedi text')
      name = input()
      pretty_print(create(name))
    else:
      # last_elem()
      pretty_print('nothing')
