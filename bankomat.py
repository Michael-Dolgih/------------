def balancemenshenulya():
  global balance
  if balance < 0:
    balance = 0
  return (balance)

try:
  balance = int(open('balance.txt', encoding= 'utf-8').read())
  balancemenshenulya()
except:
   balance = 100


def save():
  global balance
  balancemenshenulya()
  file = open('balance.txt', 'w', encoding= 'utf-8')
  file.write(str(balance))
  file.close

def D_block(vvod):
  global balance
  balance = vvod + balance
  save()
  
  
def W_block(vvod):
  global balance
  balance = balance - vvod
  save()

  
inputs = ''
while inputs.lower() != "q" :
  print('Какую команду использовать? Пополнить (D), вывести (W), проверить баланс (B) или выйти из приложения (Q)')
  inputs = ''
  inputs = input()
  if inputs.lower() == 'd':
    print('Вы выполняете операцию пополнение. Введите число. Вводимое число должно быть больше нуля!')
    try:
      vvod = int(input())
    except:
       vvod = 0
    if vvod <= 0:
       print('НУЖНО ВВЕСТИ ЧИСЛО БОЛЬШЕ НУЛЯ!!!!')
    elif vvod > 0:
            D_block(vvod)
  elif inputs.lower() == 'w':
    if balance != 0:
      print('Вы выполняете операцию вывод. Введите число. Вводимое число должно быть больше нуля!')
      try:
        vvod1 = int(input())
      except:
        vvod1 = 0
      if vvod1 > balance:
         print('Слишком большая сумма')
      elif vvod1 <= 0:
        print('НУЖНО ВВЕСТИ ЧИСЛО БОЛЬШЕ НУЛЯ!!!!')
      elif vvod1 > 0:
          W_block(vvod1)
    else:
       print('На вашем балансе нет финансов')
  elif inputs.lower() == 'b':
     print(f'Ваш баланс =', balance, 'рублей.')
  else:
     print('Команда не найдена')
print('Хорошего дня!')
