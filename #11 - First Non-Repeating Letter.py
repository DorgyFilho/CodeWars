def first_non_repeating_letter(string):
    strLow = string.lower()
    for i, let in enumerate(strLow):
        if strLow.count(let) == 1:
            return string[i]
    return ''
    
string = 'stress'
print(first_non_repeating_letter(string))
