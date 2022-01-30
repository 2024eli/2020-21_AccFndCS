#Name: Evelyn Li
#Date: 1/08/2021

from Tkinter import *

root = Tk() # Create a window.
w, h = 1000, 640
cnvs = Canvas(root, width=w, height=h, bg='white')
cnvs.pack()

data = open("lab313.txt").readlines()
data = [i.replace("\n", "").replace("\r", "") for i in data]
print len(data)

polys = []
currentList = []
xmin = -124.73
xmax = -66.95
ymin = 24.54
ymax = 49.38

total = len(data)
for i in data:
   try:
      cp = i.split(" ")
      cx = float(cp[0])
      cy = float(cp[1])
      currentList.append([cx, cy])
   except Exception, e:
      polys.append(currentList)
      currentList = []
      
      if "END_ONE_POLY" == i:
         scaled = []
         for i in polys:
            for j in i:
               scaled.append(j)
         polys = []
         
         xList = [i[0] for i in scaled]
         yList = [i[1] for i in scaled]
         
         m = 0
         xyp = []
         while m < len(xList):
            x1, y1 = xList[m], yList[m]
            xp = 0.05*w + 1.4*h*((x1 - xmin)/(xmax - xmin))
            yp = 0.03*w + 0.9*h*(1 - (y1 - ymin)/(ymax - ymin))
            xyp.append((xp, yp))
            m+=1

         cnvs.create_polygon(xyp, fill = "grey", outline = "black")
# zoom in to a place of significance (Seattle):
#cnvs.scale(ALL, xmax-xmin, ymax-ymin, 11.2, 9.6) #if you take this line out, it shows USA
       
root.mainloop() # Show window. Put at the end. 