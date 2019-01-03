def getCount(inputStr):
    num_vowels = 0
    a = inputStr.count('a')
    e = inputStr.count('e')
    i = inputStr.count('i')
    o = inputStr.count('o')
    u = inputStr.count('u')
    total = a+e+i+o+u
    num_vowels += total
    return num_vowels

inputStr = 'Dorgival'
print(getCount(inputStr))
