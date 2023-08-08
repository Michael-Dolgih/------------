massive = open('names.txt', encoding= 'utf-8').read().splitlines()


def pretty_print(massive2):
  if type(massive2) == list:
    for l in range(0, len(massive2)):
      print(f'{l+1}) {massive2[l]}') 
  else:
    print(massive2)

def inputed(pattern):
  global massive
  result = []
  for e in massive:
    if pattern in e.lower():
      result.append(e)
  save(result)

def save(res):
  file = open('result.txt', 'a', encoding= 'utf-8')
  for i in range(len(res)):
    file.write(res[i]+'\n')
  file.close

inputs = input()
if inputs == '-1':
  file = open('result.txt', 'r', encoding= 'utf-8')
  for i in file:
    print(i)
while inputs != '-1':
    inputs = ''
    inputs = input()
    if inputs == '-1':
      file = open('result.txt', 'r', encoding= 'utf-8')
      for i in file:
        print(i)
    elif inputs == 'inputed':
        pretty_print('vvedi slovo')
        pattern = input()
        pretty_print(inputed(pattern))
    else:
      pretty_print('nothing')
