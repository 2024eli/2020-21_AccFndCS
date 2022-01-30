#Name: Evelyn Li
#Date: 12/09/2020

from Tkinter import *

w, h = 640, 480

root = Tk() # Create a window.
cnvs = Canvas(root, width=w, height=h, bg='white')
cnvs.pack()

data = open("lab312.txt").read().split()
print len(data)

xList = []
yList = []

index = 0
while index < len(data):
   x = float(data[index])
   index+=1
   y = float(data[index])
   index+=1
   xList.append(x)
   yList.append(y)  

xmin = min(xList)
xmax = max(xList)
ymin = min(yList)
ymax = max(yList)
print xmin, xmax, ymin, ymax

xyp = []
j = 0

while j < len(xList): 
      x, y = xList[j], yList[j]
      xp = 0.20*w + 0.90*h*(x - xmin)/(xmax - xmin)
      yp = 0.05*w + 0.90*h*(1 - (y - ymin)/(ymax - ymin)) 
      xyp.append((xp, yp))
      j+=1

cnvs.create_polygon(xyp, fill='grey', outline='black')

root.mainloop() # Show window. Put at the end. 