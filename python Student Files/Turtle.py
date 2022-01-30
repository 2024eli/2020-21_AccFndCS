# Greg Anderson
# 7/13/12
# Turtles

from PIL import Image
from math import sin, cos, pi

class Turtle:
    def __init__(self, im, x = 0, y = 0, deg = 0, color = (0, 0, 0)):
        self.im = im   # the image onwhich this turtle resides
        self.x = x    # the x coordinate (in pixels) of this turtle
        self.y = y   # the y coordinate (in pixels) of this turtle
        self.deg = deg   # the heading (in degrees) of this turtle
        self.color = color  # the color of this turtle in the form (r, g, b)
    # Change the heading of this turtle by rotating it a given number
    #   of degrees counter-clockwise
    def turn(self, degs):
        self.deg = (self.deg + degs) % 360
    # Move this turtle forward dist (where dist is measured in pixels)
    #      drawing a line behind it
    def move(self, dist):
        newPixels = 0
        i = 0
        while i < dist:
            if self.im.getpixel((int(self.x), int(self.y))) != self.color:
                self.im.putpixel((int(self.x), int(self.y)), self.color)
                newPixels += 1
            self.x += cos(self.deg * pi / 180) # the turtles coordinates
            self.y -= sin(self.deg * pi / 180) #  after moving
            i += 1
        return newPixels

