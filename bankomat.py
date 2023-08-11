string = open('balance.txt', encoding= 'utf-8').read()
def massive():
  try:
    global string
    return(int(string))
  except:
    return(100)

def save(bal):
  file = open('balance.txt', 'w', encoding= 'utf-8').write()
  file.write(bal)
  file.close

def D_block(vvod):
  global string
  summa = vvod + int(string)
  return(summa)
  
  

print(f'Баланс =', massive(), 'рублей.')
inputs = ''
while inputs.lower() != "q" :
  print('Какую команду использовать? Пополнить (D), вывести (W), проверить баланс (B) или выйти из приложения (Q)')
  inputs = ''
  inputs = input()
  if inputs.lower() == 'd':
    print('Введите число. Вводимое число должно быть больше нуля!')
    vvod = int(input())
    if vvod <= 0:
       print('НУЖНО ВВЕСТИ ЧИСЛО БОЛЬШЕ НУЛЯ!!!!')
    elif vvod > 0:
        try:
            print(D_block(vvod))
        except:
            break

