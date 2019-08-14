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

    def show(self):
        self.canvas.pack()
        self.tk.mainloop()

    def checkbounds(self, points):
        xmin, ymin, xmax, ymax = extent(points);

        if xmax > self.width:
            raise ValueError(
                "The shape extends beyond the canvas: x=%d is greater than canvas width %d" % (xmax, self.width))

        if xmin < 0:
            raise ValueError("The minimum boundary x=%d cannot be less than 0" % xmin)

        if ymax > self.width:
            raise ValueError(
                "The shape extends beyond the canvas: y=%d is greater than window height %d " % (ymax, self.height))

        if ymin < 0:
            raise ValueError("The minimum boundary y=%d cannot be less than 0" % ymin)
