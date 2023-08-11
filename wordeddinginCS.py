def last(last_letters):
    if last_letters[-2:].lower() == "cs":
        a = len(last_letters)
        return(2**len(last_letters))
    else:
        return(last_letters[::-1])

print('Введите любые буквы:')
last_letters = input()
print(last(last_letters))