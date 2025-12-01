def first_letters_long (n):
    first = []
    for i in n:
        if len(i) > 3:
            first.append(i[0])
    return first
