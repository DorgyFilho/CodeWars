def longest_consec(strarr, k):
    n = len(strarr)
    if n == 0 or k > n or k <= 0:
        return ''
    
    longest, point = 0, 0
    
    for i in range(n - k + 1):
        lth = sum([len(s) for s in strarr[i: i+k]])
        if lth > longest: 
            longest = lth
            point = i
    return ''.join(strarr[point:point+k])

print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2), "abigailtheta")
