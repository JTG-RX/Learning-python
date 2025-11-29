#1
def fristL(n):
    Litter = []
    for i in n:
        if len(i) == 0:
            Litter.append(i)
        
    return Litter
#2
def fristL(n):
    Litter = []
    for i in n:
       for l in i:
           if l == l[0]:
            Litter.append(i)
        
    return Litter

#3
def fristL(n):
    Litter = []
    for i in n:
        Litter.append(i[0])
    return Litter 
    #just had to think simpler
