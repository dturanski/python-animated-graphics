from graphics import *

WIDTH = 500
HEIGHT = 800

graphics = Graphics(WIDTH, HEIGHT)


class BouncingShape:
    def __init__(self, shape, xspeed, yspeed):
        self.shape = shape
        self.xspeed = xspeed
        self.yspeed = yspeed


shape1 = BouncingShape(graphics.rectangle((250, 250), (350, 350), fill="orange"), 4, 5)

shape2 = BouncingShape(graphics.circle((120, 160), 50, fill="pink"), 30, 40)

shape3 = BouncingShape(graphics.circle((200, 400), 20, fill="green"), 2, 20)


def bounce(shape):
    graphics.move(shape.shape, (shape.xspeed, shape.yspeed))
    topleft, bottomright = graphics.coords(shape.shape)
    xmin, ymin = topleft
    xmax, ymax = bottomright

    if ymax >= HEIGHT or ymin <= 0:
        shape.yspeed = -shape.yspeed
    if xmax >= WIDTH or xmin <= 0:
        shape.xspeed = -shape.xspeed


while True:
    bounce(shape1)
    bounce(shape2)
    bounce(shape3)
    graphics.update()

graphics.show()
