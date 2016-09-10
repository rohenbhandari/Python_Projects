import numpy as np

t = input('Number of test cases : ')
cp = 0
op = 0
while t > 0:
  s = raw_input('Enter string : ')
  for i in range(0, len(s) + 1):
    if(s[i] == '1'):
      cp = cp + 1
      if(cp == 11):
        print 'WIN'
        break
    elif(s[i] == '0'):
      op = op + 1
      if(op == 11):
        print 'LOSE'
        break  
    if(cp != 10 and op != 10):
      if(s[i] == '1' and s[i + 1] == '1'):
        print 'WIN'
        break
      elif(s[i] == '0' and s[i + 1] == '0'):
        print 'LOSE'
        break
      
  t -= 1
