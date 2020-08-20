# This will import the graphics tools we will use in our program.
from graphics import *

# This will create a space on which we will draw our graphics.
graphics = Graphics(500, 800)

graphics.show_grid(50)

graphics.circle((100, 100), 50, fill="yellow")

graphics.rectangle((200, 300), (450, 550), fill="orange")

graphics.polygon([(200, 300), (450, 300), (325, 150)], fill="brown")

graphics.rectangle((290, 425), (360, 550), fill="red")

graphics.rectangle((220, 320), (300, 400), fill="white")

graphics.rectangle((350, 320), (430, 400), fill="white")

graphics.line((220,360),(300,360))

graphics.line((260,320),(260,400))

graphics.line((350,360),(430,360))

graphics.line((390,320),(390,400))

graphics.show()
