def only_strings(n):
    strings =[]
    for i in n:
        if i == str(i):
            strings.append(i)
    return strings
