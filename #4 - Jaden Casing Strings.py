def toJadenCase(string):
    words = string.split(' ')
    newStr = []
    for word in words:
        newStr.append(word.capitalize())
    return ' '.join(newStr)
  
string = "How can mirrors be real if our eyes aren't real"
print(toJadenCase(string))
