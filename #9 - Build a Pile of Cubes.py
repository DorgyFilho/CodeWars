def find_nb(m):
    vol = 0
    n = 1
    while vol < m:
        vol += n**3
        if vol == m:
            return n
        n += 1
    return -1
