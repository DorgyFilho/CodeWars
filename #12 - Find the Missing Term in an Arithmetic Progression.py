def find_missing(sequence):
    period = ((sequence[-1] - sequence[0])/len(sequence))
    for a, b in enumerate(sequence[1:]):
        if b - sequence[a] != period:
            return b - period

print(find_missing([1, 2, 3, 4, 6, 7, 8, 9]))
