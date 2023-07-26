#python 3.6.9

def eto_chislo(chislo):
  try:
      int(chislo)
      return True
  except:
        return False
summa=0
chisla= '0'
for simvol in input():
  if eto_chislo(simvol) == True:
    chisla+=simvol
    print(simvol)
  else:
    summa+=int(chisla)
    chisla='0'
summa+= int(chisla)
chisla= '0'
print('chisla', chisla)
print('summa', summa)
