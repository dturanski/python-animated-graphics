from tkinter import *
import sys


def extent(points):
    """
    Computes the extent of a list of (x,y) points
    :param points: a list of (x,y) points
    :return: the extent as xmin, ymin, xmax, ymax
    """
    xmax = -sys.maxsize - 1
    ymax = -sys.maxsize - 1
    ymin = sys.maxsize
    xmin = sys.maxsize

    for p in points:
        x, y = p
        if x < xmin:
            xmin = x
        if x > xmax:
            xmax = x
        if y < ymin:
            ymin = y
        if y > ymax:
            ymax = y

    return xmin, ymin, xmax, ymax


class Graphics:
    """
    Wraps tk graphics primitives to make graphics concepts easier for beginners.
    """

    def __init__(self, w, h):
        self.tk = Tk()
        self.width = w
        self.height = h
        self.canvas = Canvas(self.tk, width=self.width, height=self.height)
        self.canvas.pack()

    def circle(self, center, radius, **kwargs):
        x, y = center
        self.checkbounds([(x - radius, y - radius), (x + radius, y + radius)])

        return self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, kwargs)

    def rectangle(self, topleft, bottomright, **kwargs):

        self.checkbounds([topleft, bottomright])
        xmin, ymin, xmax, ymax = extent([topleft, bottomright])
        return self.canvas.create_rectangle(xmin, ymin, xmax, ymax, kwargs)

    def polygon(self, points, **kwargs):
        self.checkbounds(points)
        return self.canvas.create_polygon(points, kwargs)

    def line(self, a, b, **kwargs):
        self.checkbounds([a, b])
        xmin, ymin, xmax, ymax = extent([a, b])
        return self.canvas.create_line(xmin, ymin, xmax, ymax, kwargs)

    def coords(self, obj):
        points = self.canvas.coords(obj)
        coords = []
        for i in range(0, len(points), 2):
            coords.append((points[i], points[i + 1]))
        return coords

    def move(self,obj, delta):
        self.canvas.move(obj,delta[0], delta[1])

    def update(self, after=20):
        self.canvas.update()
        self.canvas.after(after)


    def show(self):
        self.tk.mainloop()

    def checkbounds(self, points):
        xmin, ymin, xmax, ymax = extent(points);

        if xmax > self.width:
            print(
                "WARNING:The shape extends beyond the canvas: x=%d is greater than canvas width %d" % (
                xmax, self.width))

        if xmin < 0:
            print("WARNING: The minimum boundary x=%d cannot be less than 0" % xmin)

        if ymax > self.height:
            print(
                "WARNING:The shape extends beyond the canvas: y=%d is greater than window height %d " % (
                ymax, self.height))

        if ymin < 0:
            print("WARNING: The minimum boundary y=%d cannot be less than 0" % ymin)

class Group:
    def __init__(self, graphics):
        self.graphics = graphics
        self.objects = []

    def add(self, object):
        self.objects.append(object)

    def move(self, delta):
        for obj in self.objects:
            self.graphics.move(obj,delta)
        self.graphics.update()


