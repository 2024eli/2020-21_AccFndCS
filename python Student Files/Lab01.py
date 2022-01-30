# Name: Evelyn Li
# Date: 10/14/2020

from random import random

n=5
m=2*n+1
steps=0
j=n+1
while 1<=j<=m:
   if random()<0.5:
      j+=1
   else:
      j-=1
   steps+=1
   print
   k=1
   while k<=m:
      if k==j:
         print 'X',
      elif k==n+1:
         print '|',
      else:
         print '-',
      k+=1
   print
print (1.0*steps)

