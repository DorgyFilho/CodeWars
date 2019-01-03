def lost_chars(X):
    begin, end = X[0], X[-1]
    return sorted(set(range(begin, end+1)).difference(X))

def find_missing_letter(chars):
    elem = list(map(ord, chars))
    i = lost_chars(elem)
    return chr(i[0])
    
chars = ['a', 'b', 'c', 'd', 'f']
print(find_missing_letter(chars))
