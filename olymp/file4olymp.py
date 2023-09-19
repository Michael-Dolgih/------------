




n = int(input())
m = int(input())

if n > m:
    x = n
    n = m
    m = x
otvet = n
while n > 0 and m > 0:
    otvet += m - 1 + n - 1
    n -= 2
    m -= 2
print(otvet)