from graphics import *

WIDTH = 500
HEIGHT = 800

graphics = Graphics(WIDTH, HEIGHT)

class Ball:
    def __init__(self, shape, xspeed, yspeed):
        self.shape = shape
        self.xspeed = xspeed
        self.yspeed = yspeed


ball1 = Ball(graphics.rectangle((250, 250), (350,350), fill="orange"), 4, 5)

ball2 = Ball(graphics.circle((120, 160), 50, fill="pink"), 30, 40)

ball3 = Ball(graphics.circle((200, 400), 20, fill="green"), 2, 20)



def move_ball(ball):
    graphics.move(ball.shape, (ball.xspeed, ball.yspeed))
    topleft, bottomright = graphics.coords(ball.shape)
    xmin, ymin = topleft
    xmax, ymax = bottomright

    if ymax >= HEIGHT or ymin <= 0:
        ball.yspeed = -ball.yspeed
    if xmax >= WIDTH or xmin <= 0:
        ball.xspeed = -ball.xspeed


while True:
    move_ball(ball1)
    move_ball(ball2)
    move_ball(ball3)
    graphics.update()

graphics.show()
