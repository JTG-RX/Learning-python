def square_evens(n):
    newlist = []
    for i in n:
        if i % 2 == 0:
           i = i **2
           newlist.append(i)
    return newlist
