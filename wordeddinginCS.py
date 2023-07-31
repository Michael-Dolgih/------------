last_letters = input()
print(last_letters[-1])
print(last_letters[-2:])
if last_letters[-2:].lower() == "cs":
    a = len(last_letters)
    print(int(a)**2)
else:
    print(last_letters[::-1])