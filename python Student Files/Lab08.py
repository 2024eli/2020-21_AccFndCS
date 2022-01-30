#Name: Evelyn Li
#Date: 11/04/2020

from PIL import Image
import random

#P1 = (x1, y1) = (0.5, 0.1)
#P2 = (x2, y2) = (0.1, 0.9)
#P3 = (x3, y3) = (0.9, 0.9)

img = Image.new("RGB", (600, 600), (255, 255, 255))

x1 = 300
y1 = 60
img.putpixel((x1, y1), (255, 0, 0))

x2 = 60
y2 = 540
img.putpixel((x2, y2), (255, 0, 0))

x3 = 540
y3 = 540
img.putpixel((x3, y3), (255, 0, 0))

x = 0
y = 0

count = 0

f = open("lab08.txt", "w")

for repeat in range(1, 30001):
   whatpoint = random.randint(1,3)
   if whatpoint == 1:
      x = ((x + x1) / 2)
      y = ((y + y1) / 2)
   if whatpoint == 2:
      x = ((x + x2) / 2)
      y = ((y + y2) / 2)
   if whatpoint == 3:
      x = ((x + x3) / 2)
      y = ((y + y3) / 2)
   #to do: unique pixels
   if (255, 255, 255) == img.getpixel((x, y)):
      img.putpixel((x, y), (255, 0, 0))
      count+=1
      print repeat, count
      f.write(str(repeat) + " " + str(count) + "\n")
img.save("lab08.png")
import webbrowser
webbrowser.open("lab08.png")
f.close()