def unique_in_order(iterable):
    char = None
    final = list()
    for word in iterable[0:]:
        if word != char:
            final.append(word)
            char = word
    return final

print(unique_in_order('AAAABBBCCDAABBB'))
