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

def massives_odinak():
  print('massives_odinak')
  global massive
  massive2 = open('result.txt', 'r', encoding= 'utf-8').read().splitlines()
  for stroka in massive:
    if stroka not in massive2:
      print(f'DEBUG0 : {stroka}')
      return False
  print(f'DEBUG1 : {massive}')
  return True

inputs = ''
while inputs != '-1':
  inputs = ''
  inputs = input()
  if inputs == 'inputed':
    pretty_print('vvedi slovo')
    pattern = input()
    pretty_print(inputed(pattern))
    if massives_odinak():
      break
  else:
    pretty_print('nothing')
pretty_print(open('result.txt', 'r', encoding= 'utf-8').read().splitlines())