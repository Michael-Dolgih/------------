import random
#Ограничение по времени: 0.5 секунд
#В крайних клетках полоски шириной в одну клетку и длиной в N клеток сидят лягушка и кузнечик: лягушка в клетке № 1, кузнечик в клетке № N. Каждую секунду лягушка прыгает в сторону
#кузнечика, и одновременно кузнечик прыгает в сторону лягушки. Лягушка может прыгать только
#на две или на три клетки, кузнечик — только на одну или на две клетки. За какое наименьшее
#время они смогут оказаться в одной клетке?
def pri(l,k, d, step):
  stroka = list('_'*d)
  stroka[l-1]= '+'
  stroka[k-1]= '-'
  print (f"{step}) {''.join(stroka)}")

try:
    n = int(input())
except:
    print('error1')
99
if 2 <= n or n <= 2*10**9:
    kuznechik = n
    lyaguha = 1
    secunda = 0
    while kuznechik >= lyaguha:
      secunda += 1
      pri(lyaguha, kuznechik, n, secunda)
      lyaguha += 3
      kuznechik -= 2
    print('ok')
    print('seconds =', secunda)



