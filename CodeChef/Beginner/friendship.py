import numpy as np
  
t = input('Number of test cases : ')
while t > 0:
  n = input('Number of friends : ')
  d = np.zeros(n)
  i = 0
  f = 0
  for i in range(0, n):
    d[i] = input('Days : ')
    for j in range(0, i):
      if(d[i] != d[j]):
        f += 1
  
  print 'number of friendships saved is :', f
  
  t = t - 1
