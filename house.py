from graphics import *

graphics = Graphics(1000, 800)

circle = graphics.circle((100, 100), 50, fill="yellow")

points = [(250, 150), (350, 250), (150, 250)]

triangle = graphics.polygon(points, outline='black', fill='brown', width=2)

rectangle = graphics.rectangle((150, 250),(350, 450), fill='orange')

graphics.show()