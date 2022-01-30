# Name: Evelyn Li
# Date: 10/21/2020

from math import pi, cos, sin

t=0.0 #seconds
x=0.0 #meters
y=0.0
v0=26.82 #meters per second
theta=30.0*(pi/180) #30 degrees in radians
dt=0.001
vy=v0*sin(theta)
vx=v0*cos(theta)
g = -9.81 #meters per second squared
c1=0.00
ax = (-c1*vx) 			
ay = (g-c1*vy)

f=open("file.txt", "w")	 
while y>=0.0:
   x+=(vx*dt)
   y+=(vy*dt)
   vx+=(ax*dt)
   vy+=(ay*dt)
   t+=dt
   print t, x, y, (0.5*g*t*t+v0*sin(theta)*t) 
   print x, y
   f.write(str(x) + " " + str(y) + "\n")
f.close()





