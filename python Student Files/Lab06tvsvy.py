#Name: Evelyn Li
#Date: 10/25/2020

from math import pi, cos, sin

v0 = 0.0 #initial speed of the object
theta = pi/3 #initial angle = 60 degrees
vx = v0 * cos(theta)
vy = v0 * sin(theta)
x = 0.0 #start position
y = 1500.0 #ground
t = 0.0 #start time
dt = 0.001 #the small line
g = -9.81 #gravity
c1 = 0.5 #drag
vw = 0.44704 #wind speed
ax = 0.0 #initial horizontal acceleration
ay = g #initial vertical acceleration

f = open("lab06tvsvy.txt", "w")

print t, x, y, vx, vy, ax, ay 

while y>=0.0:
   y += vy * dt
   x += vx * dt
   vy += ay * dt
   vx += ax * dt
   ay = g - c1 * vy
   ax = -c1 * (vx - vw)
   t += dt
   print t, x, y, vx, vy, ax, ay 
   f.write(str(t) + " " + str(vy) + "\n")

print 
f.close()