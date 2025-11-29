def odds(n): 
  count = 0 
  for i in n: 
    if i % 2 != 0: 
      count = count + 1 
  return count
