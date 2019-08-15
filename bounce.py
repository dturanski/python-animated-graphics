from graphics import *
from time import sleep

WIDTH = 1000
HEIGHT = 600

graphics = Graphics(WIDTH, HEIGHT)

ball1 = graphics.circle((250, 250), 80, fill="orange")
xspeed1 = 4
yspeed1 = 5

ball2 = graphics.circle((120, 160), 50, fill="pink")
xspeed2 = 30
yspeed2 = 40

ball3 = graphics.circle((200, 400), 20, fill="green")
xspeed3 = 2
yspeed3 = 20


def move_ball(ball, xspeed, yspeed):
    graphics.move(ball, (xspeed, yspeed))
    topleft, bottomright = graphics.coords(ball)
    xmin, ymin = topleft
    xmax, ymax = bottomright

    if ymax >= HEIGHT or ymin <= 0:
        yspeed = -yspeed
    if xmax >= WIDTH or xmin <= 0:
        xspeed = -xspeed
    return xspeed, yspeed


while True:
    xspeed1, yspeed1 = move_ball(ball1, xspeed1, yspeed1)
    xspeed2, yspeed2 = move_ball(ball2, xspeed2, yspeed2)
    xspeed3, yspeed3 = move_ball(ball3, xspeed3, yspeed3)
    sleep(0.01)

graphics.show()
