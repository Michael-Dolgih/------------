from datetime import datetime

def chislo(inp):
    if inp== '0':
      return [" ####",
      " #  #",
      " #  #",
      " ####"]    
    elif inp=='1':
      return ["   # ",
      "  ## ",
      "   # ",
      " ####" ]
    elif inp=='2':
      return ["  ## ",
      " #  #",
      "   # ",
      " ####"]
    elif inp=='3':
      return [" ## ",
      " __#",
      "   #",
      " ## "] 
    elif inp=='4':
      return [" #  #",
      " #__#",
      "    #",
      "    #"] 
    elif inp=='5':
      return [" ####",
      " #___",
      "    #",
      " ####"]
    elif inp=='6':
      return [" ####",
      " #___",
      " #  #",
      " ####"]
    elif inp=='7':
      return [" ####",
      "   # ",
      "  #  ",
      " #   "]
    elif inp=='8':
      return [" ####",
      " #__#",
      " #  #",
      " ####"]
    elif inp=='9':
      return [" ####",
      " #__#",
      "    #",
      " ####"]
    elif inp==':':
      return ["  #  ",
      "     ",
      "  #  ",
      "     "]
    else:
      return [' ', ' ', ' ', ' ']

now = datetime.now()
verh=''
verh_sered=''
niz_sered=''
niz=''
for l in now.strftime("%H:%M"):
  verh1,verh_sered1,niz_sered1,niz1 = chislo(l) 
  verh+=verh1
  verh_sered+=verh_sered1
  niz_sered+=niz_sered1
  niz+=niz1
print(verh)
print(verh_sered)
print(niz_sered)
print(niz)
