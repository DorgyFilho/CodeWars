def camel_case(string):
    Str = string.title()
    newStr = Str.replace(' ', '')
    return newStr
    
   
string = 'hello case'
print(camel_case(string))
