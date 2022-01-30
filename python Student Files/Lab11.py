#Name: Evelyn Li
#Date: 11/13/2020

from random import random
from PIL import Image
from math import cos, sin, pi
from Turtle import *

img = Image.new("RGB", (640, 480), (204, 204, 204))

trials = 0
totalNewPixels = 0 
f = open("lab11.txt", "w")

while trials < 1000:
   t1 = Turtle(img, 320, 460, 90, (0, 0, 0))
   trials += 1
   n = 150 
   newPixels = 0
   t1.move(n)
   for x in range(1, 9):
      if random() < 0.5:
         t1.turn(30)
      else:
         t1.turn(-30)
      n = n * 2 / 3 
      count = t1.move(n)
      newPixels += count
   totalNewPixels += newPixels
   print trials, totalNewPixels, newPixels
   f.write(str(trials) + " " + str(totalNewPixels) + " " + str(newPixels) + "\n")
      
img.save("lab11.png")
import webbrowser
webbrowser.open("lab11.png")
f.close()