# Name: Evelyn Li
# Date: 10/21/2020

from math import pi, cos, sin

v0 = 15 #initial speed 
theta = pi/3 #initial angle = 60 degrees
vw = -10
   
f = open("lab05b.txt", "w")

for vw in range(-10, 31):
   vx = v0 * cos(theta)
   vy = v0 * sin(theta)
   x = 0.0 #start position
   y = 0.0 #ground
   t = 0.0 #start time
   dt = 0.001 #the small line
   g = -9.81 #gravity
   c1 = 0.5 #drag
   ax = 0 #initial horizontal acceleration
   ay = g #initial vertical acceleration
   
   while y>=0.0:
      y += vy * dt
      x += vx * dt
      vy += ay * dt
      vx += ax * dt
      ay = g - c1 * vy
      ax = -c1 * (vx - vw)
      t += dt
   f.write(str(t) + " " + str(x) + " " + str(vw) + "\n")    
   vw += 1.0

f.close()
