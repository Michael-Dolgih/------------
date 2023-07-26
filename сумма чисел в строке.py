def otbor_chisel(vsyakoe):
 try:
     return int(vsyakoe)
 except:
     return 0 

otvet= 0
for bukva in input():
  otvet+=otbor_chisel(bukva)
print(otvet)
