
def input_poke():
    global dict
    print('vvod name')
    name  = input()
    print("vvod color")
    color  = input()
    dict.append({'name': name , 'color': color})

dict = []
print('vvod kol poke')
dlin=int(input())
for chislo in range(0, dlin):
  input_poke()    
print(dict)
for ele in dict:
  print(ele.get('name'))