#Name: Evelyn Li
#Date: 11/11/2020

from Turtle import *
from PIL import Image
from math import cos, sin, pi

img = Image.new("RGB", (600, 600), (255, 255, 255))
t1 = Turtle(img, 100, 200, 0, (255, 0, 0))
t2 = Turtle(img, 400, 200, 60, (0, 255, 0))
t3 = Turtle(img, 250, 350, 270, (0, 0, 255))

y = 200

for x in range(6):
   t1.move(80)
   t1.turn(60)

for x in range(6):
   t2.turn(60)
   for x in range(6):
      t2.move(60)
      t2.turn(60)

for x in range(30):
   t3.move(y)
   t3.turn(-90)
   y-=10

img.save("lab10.png")
import webbrowser
webbrowser.open("lab10.png")