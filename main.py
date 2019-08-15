# This will import the graphics tools we will use in our program.
from graphics import *

# This will create a space on which we will draw our graphics.
graphics = Graphics(500, 800)

line = graphics.line((0,360),(600,360))

print(graphics.coords(line))

graphics.show()