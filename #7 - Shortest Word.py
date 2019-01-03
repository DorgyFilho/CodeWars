def find_short(s):
    l = s.split(' ')
    l.sort(key=len)
        
    return len(l[0]) # l: shortest word length
