#1
def greater_than_5(n): 
  over5 = [] 
  for i in n:  
  if i >5: 
    over5.append(i) 
  return over5
#2
def only_strings(n):
    strings =[]
    for i in n:
        if type(i) == str:
            strings.append(i)
    return strings
