def eto_chislo(chislo):
  try:
      int(chislo)  
      return True
  except:
    return False

chisla= 0
bukvi= 0
for bukva in input():
  if eto_chislo(bukva):
    chisla+= 1
  else:
    bukvi+= 1
print('буквы:',bukvi)
print('числа:',chisla)