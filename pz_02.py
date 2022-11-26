def palindrom(word):
    return str(word) == str(word)[::-1]


print(palindrom(1231))