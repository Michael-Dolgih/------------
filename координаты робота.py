x=0
y=0
for kakayato_bukva in input():
  if kakayato_bukva== "d" or kakayato_bukva== "D":
    y+= -1
  elif kakayato_bukva== "u" or kakayato_bukva== "U":
    y+= 1
  elif kakayato_bukva== "l" or kakayato_bukva== "L":
    x+= -1
  elif kakayato_bukva== "r" or kakayato_bukva== "R":
    x+= 1
print("x=", x, "y=", y)