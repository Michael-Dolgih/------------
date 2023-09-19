# n = int(input())
# m = int(input())

# def vichesl(n, m):
#     masive = []
#     while True:
#         if m < n:
#           masive.append(m)
#         else:
#           masive.append(n)
#         m = m - n
#         n = n - 1
#         if m <= 0:
#             return(masive)
#         elif n <= 0:
#             return([0])
# print(vichesl(n, m))

# print('v2')

# def vichesl1(n, m):
#     while True:
#         if m < n:
#           print(m)
#         else:
#           print(n)
#         m = m - n
#         n = n - 1
#         if m <= 0:
#             break
#         elif n <= 0:
#             print(0)
#             break
# vichesl1(n, m)

n = int (input ())
m = int (input ())
if (1 + n) * n // 2 < m :
  print (0)
else:
  while m > n :
    print (n)
    m -= n
    n -= 1
print (m)