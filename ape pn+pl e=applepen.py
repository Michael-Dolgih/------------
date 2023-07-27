#python 3.6.
def input0(inp, cif):
  try:    
    return inp[cif]
  except:
    return ''
  
inputs=input().strip()
inputs_n2=input().strip()
otvet=''
dlina=''
if len(inputs) < len(inputs_n2):
  dlina = len(inputs_n2)
else:
  dlina = len(inputs)
for cifra in range(0, dlina, 1):
  otvet+=input0(inputs, cifra)+input0(inputs_n2, cifra)
print(otvet)