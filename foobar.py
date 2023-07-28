def foobar(a, b): 
    if a ==20 or b == 20:
        return(b)
    else:
        return(a+b)
try:
  print("first number")
  a = int(input())
  print("second number")
  b = int(input())
  print(foobar(a, b))
except:
  print("Ты чаво, эт не число!")