#Name: Evelyn Li
#Date: 11/06/2020

from PIL import Image

#P1 = (x1, y1) = (0.05, 0.05)
#P2 = (x2, y2) = (0.95, 0.05)
#P3 = (x3, y3) = (0.95, 0.95)
#P4 = (x4, y4) = (0.05, 0.95)

def drawLine(ptX1, ptY1, ptX2, ptY2):
   t = 0.0
   while t < 1.0:
      x = int ((ptX1 + t * (ptX2 - ptX1)))
      y = int ((ptY1 + t * (ptY2 - ptY1)))
      img.putpixel((x, y),(255, 204, 0)) 
      t += 0.001

img = Image.new("RGB", (600, 600), (0, 0, 255))

x1 = 30
y1 = 30
img.putpixel((x1, y1), (255, 204, 0))

x2 = 570
y2 = 30
img.putpixel((x2, y2), (255, 204, 0))

x3 = 570
y3 = 570
img.putpixel((x3, y3), (255, 204, 0))

x4 = 30
y4 = 570
img.putpixel((x4, y4), (255, 204, 0))

drawLine(x1, y1, x2, y2)
drawLine(x2, y2, x3, y3)
drawLine(x3, y3, x4, y4)
drawLine(x4, y4, x1, y1)

for repeat in range(50): 
   x1 = 0.1 * (x2 - x1) + x1
   y1 = 0.1 * (y2 - y1) + y1
   x2 = 0.1 * (x3 - x2) + x2
   y2 = 0.1 * (y3 - y2) + y2
   x3 = 0.1 * (x4 - x3) + x3
   y3 = 0.1 * (y4 - y3) + y3
   x4 = 0.1 * (x1 - x4) + x4
   y4 = 0.1 * (y1 - y4) + y4
   drawLine(x1, y1, x2, y2)
   drawLine(x2, y2, x3, y3)
   drawLine(x3, y3, x4, y4)
   drawLine(x4, y4, x1, y1)
  
img.save("lab09.png")
import webbrowser
webbrowser.open("lab09.png")