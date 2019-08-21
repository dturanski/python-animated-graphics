from graphics import *

WIDTH = 600
HEIGHT = 600

graphics = Graphics(WIDTH, HEIGHT)

ball = graphics.circle((120, 160), 50, fill="pink")
boundary = graphics.coords(ball)
print(boundary)

xspeed = 3
yspeed = 4

while True:
    graphics.move(ball, (xspeed, yspeed))
    boundary = graphics.coords(ball)

    top_left = boundary[0]
    bottom_right = boundary[1]

    left = top_left[0]
    top = top_left[1]
    right = bottom_right[0]
    bottom = bottom_right[1]

    if bottom >= HEIGHT or top <= 0:
        yspeed = -yspeed
    if right >= WIDTH or left <= 0:
        xspeed = -xspeed
    graphics.update()
