#Name: Evelyn Li
#Date: 12/16/2020

from Tkinter import *

w, h = 640, 480

root = Tk() # Create a window.
cnvs = Canvas(root, width=w, height=h, bg='white')
cnvs.pack()

data = open("lab313AL.txt").read().split()
print len(data)

xList = []
yList = []

x1List = []
y1List = []

index = 0
count = 0
while count < 2:
   if "END_ONE_POLY" in data[index]:
      count += 1
      index += 1
   if data[index].isalpha() or "END_ALL_POLY" in data[index] or "END_FILE" in data[index]:
      index += 1
   else:
      if count < 1:
         x = float(data[index])
         index+=1
         y = float(data[index])
         index+=1
         xList.append(x)
         yList.append(y)  
      elif count == 1:
         x1 = float(data[index])
         index+=1
         y1 = float(data[index])
         index+=1
         x1List.append(x1)
         y1List.append(y1) 

xmin = min(xList)
xmax = max(xList)
ymin = min(yList)
ymax = max(yList)
print xmin, xmax, ymin, ymax

xyp = []

x1min = min(x1List)
x1max = max(x1List)
y1min = min(y1List)
y1max = max(y1List)
print x1min, x1max, y1min, y1max

xyp1 = []

j = 0
while j < len(xList): 
      x, y = xList[j], yList[j]
      xp = 0.29*w + 0.65*h*(x - xmin)/(xmax - xmin)
      yp = 0.05*w + 0.90*h*(1 - (y - ymin)/(ymax - ymin))
      xyp.append((xp, yp))
      j+=1

cnvs.create_polygon(xyp, fill='grey', outline='black')

k = 0
while k < len(x1List):
      x1, y1 = x1List[k], y1List[k]
      xp1 = 0.315*w + 0.04*h*(x1 - x1min)/(x1max - x1min)
      yp1 = 0.715*w + 0.01*h*(1 - (y1 - y1min)/(y1max - y1min))
      xyp1.append((xp1, yp1))
      k+=1

cnvs.create_polygon(xyp1, fill='grey', outline='black')

root.mainloop() # Show window. Put at the end. 