import os
if 'TK_SILENCE_DEPRECATION' not in os.environ:
    os.environ['TK_SILENCE_DEPRECATION']='1'
from tkinter import Tk,Canvas,Label
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
        self.width = w + 10
        self.height = h + 10
        self.canvas = Canvas(self.tk, width=self.width, height=self.height)
        self.canvas.pack()

    def circle(self, center, radius, **kwargs):
        x, y = center
        self.checkbounds([(x - radius, y - radius), (x + radius, y + radius)])

        return self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, kwargs)

    def show_grid(self, size=50, color='black'):
        w = self.width # Get current width of canvas
        h = self.height -20 # Get current height of canvas

        # Creates all vertical lines at intevals of 100
        for i in range(0, w, size):
            self.line((i, 0), (i, h), fill=color, tag='grid_line')
            label = Label(self.canvas, text=str(i),fg='red')
            x_off = 0
            if i > 0 :
                x_off = 15
            label.place(x=i-x_off,y=h)

        # Creates all horizontal lines at intevals of 100
        for i in range(0, h, size):
           
            label = Label(self.canvas, text=str(i),fg='red')
            y_off = 0
            if i > 0 :
                y_off = 15
            label.place(x=0,y=i - y_off)
            self.line((0, i), (w, i), fill=color, tag='grid_line')

    def hide_grid(self):
        self.canvas.delete('grid_line')

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

    def coords(self, obj, *args):
        points = self.canvas.coords(obj,*args)
        coords = []
        for i in range(0, len(points), 2):
            coords.append((points[i], points[i + 1]))
        return coords

    def move(self, obj, delta):
        self.canvas.move(obj, delta[0], delta[1])

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

    def add(self, obj):
        self.objects.append(obj)

    def move(self, delta):
        for obj in self.objects:
            self.graphics.move(obj, delta)
        self.graphics.update()
