#Name: Evelyn Li
#Date: 10/28/2020

from PIL import Image

#sizes (side lengths)
sizes = [600, 1000, 2000, 4000, 8000, 10000]

for size in sizes:
   img = Image.new("RGB", (size, size), (51, 51, 51))
   count = 0
   for xp in range(size):
      x = (xp + 0.5)/size
      for yp in range(size):
         y = (yp + 0.5)/size
         if (x * x + y * y <= 1.0):
            img. putpixel((xp, yp), (204, 204, 204))
            count += 1
   print size, ", pi =", (count/(0.25 * size * size)), ", pixels: ", count
   if size == 600:
      img.save("quartercircle.png")
import webbrowser
webbrowser.open("quartercircle.png")