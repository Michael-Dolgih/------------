import PySimpleGUI as sg

def balancemenshenulya():
  global balance
  if balance < 0:
    balance = 0
  return (balance)

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
  if vvod <= balance:
    balance = balance - vvod
  else:
    return ''
  save()

try:
  balance = int(open('balance.txt', encoding= 'utf-8').read())
  balancemenshenulya()
except:
   balance = 100

# Demonstrates a number of PySimpleGUI features including:
#   Default element size
#   auto_size_buttons
#   Button
#   Dictionary return values
#   update of elements in form (Text, Input)

sg.theme('DarkGrey10')

layout = [[sg.Text('Your balance:')],
          [sg.Text(str(balance), size=(15, 1), font=('Helvetica', 18),
            text_color='LightBlue', key='out')],
          [sg.Text('', key= 'error')],
          [sg.Input('', size=(26, 1), key='input')],
          [sg.Button('Withdraw'), sg.Button('Quit')],
          [sg.Button('1'), sg.Button('2'), sg.Button('3')],
          [sg.Button('4'), sg.Button('5'), sg.Button('6')],
          [sg.Button('7'), sg.Button('8'), sg.Button('9')],
          [sg.Button('Deposit'), sg.Button('0'), sg.Button('Clear')],
          ]

window = sg.Window('Банкомат', layout,
                   default_button_element_size=(6, 2),
                   auto_size_buttons=False,
                   grab_anywhere=False)


# Loop forever reading the form's values, updating the Input field
keys_entered = ''
while True:
    event, values = window.read()  # read the form
    window['out'].update(balance)
    window['error'].update('')
    if event == sg.WIN_CLOSED:  # if the X button clicked, just exit
        break
    if event == 'Quit':
       break
    elif event == 'Clear':  # clear keys if clear button
        keys_entered = ''
        window['input'].update('')
    elif event in '1234567890':
        keys_entered = values['input']  # get what's been entered so far
        keys_entered += event  # add the new digit
        window['input'].update(keys_entered)
    elif event == 'Deposit':
       D_block(int(values['input']))
       window['out'].update(keys_entered)
       window['input'].update('')
       window['out'].update(balance)
    elif event == 'Withdraw':
       w = W_block(int(values['input']))
       if w == '':
          window['error'].update('нe достаточно финансов')
       window['out'].update(keys_entered)
       window['input'].update('')
       window['out'].update(balance)

    # change the form to reflect current key string
window.close()