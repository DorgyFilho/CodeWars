def get_middle(s):
    if len(s) == 0:
        return ''
    elif len(s) % 2 != 0:
        return s[len(s)//2]
    elif len(s) % 2 == 0:
        return s[len(s)//2 - 1] + s[len(s)//2]

print(get_middle('Dorgival')) 
