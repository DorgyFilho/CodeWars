def friend(x):
    FourName = []
    for name in x:
        if len(name) == 4:
            FourName.append(name)
    return FourName

print(friend(["Ryan", "Kieran", "Mark"]))
