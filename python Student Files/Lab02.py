# Name: Evelyn Li
# Date: 10/14/2020

from random import random

n=5
m=2*n+1
steps=0
j=n+1
trial=0
totalsteps=0
numtrials = 10000
while trial<numtrials:
   j=n+1
   steps=0
   while 1<=j<=m:
      if random()<0.5:
         j+=1
      else:
         j-=1
      totalsteps+=1
      steps+=1
      k=1
      while k<=m:
         k+=1
   trial+=1
   print trial, (1.0*steps)
print 'avg',(1.0*totalsteps)/numtrials


