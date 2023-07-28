def greeting(name, familia, vozv): 
    if int(vozv) < 18:
        return(f"Привет, {name} {familia}. Тебе меньше 18 лет, но начать учиться программировать никогда не рано")
    else:
        return(f"Привет, {name} {familia}. Самое время заняться делом!")

print("Your name")
name = input()
print("your familia")
familia = input()
print('Your age')
vozv = input()
print(greeting(name, familia, vozv))