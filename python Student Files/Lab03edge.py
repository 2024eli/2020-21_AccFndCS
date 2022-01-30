# Name: Evelyn Li
# Date: 10/16/2020

from random import random

n=1
while n<=25:
   m=2*n+1
   steps=0
   j=n+1
   trial=1
   match=0
   totalsteps=0
   veryFirstStep=0
   veryFirstEdge=0
   numtrials = 10000
   while trial<=numtrials:
      j=n+1
      steps=0
      veryFirstStep=0
      veryFirstEdge=0
      while 1<=j<=m:
         if random()<0.5:
            j+=1
            veryFirstStep = 1
            if j==m and veryFirstEdge==0:
               veryFirstEdge+=1
         else:
            j-=1
            veryFirstStep = -1
            if j==1 and veryFirstEdge==0:
               veryFirstEdge-=1
         totalsteps+=1
         steps+=1
         k=1
         while k<=m:
            k+=1
      trial+=1
      if veryFirstStep==1 and veryFirstEdge==1:
         match+=1
      if veryFirstStep==-1 and veryFirstEdge==-1:
         match+=1
   print n,(100.0*match)/numtrials
   n+=1



