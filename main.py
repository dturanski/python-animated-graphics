from tkinter import * # version 3.x

tk = Tk()

frame = Frame(tk)
canvas = Canvas(frame) # use canvas

frame.pack(fill = BOTH, expand = 1)
canvas.pack(fill = BOTH, expand = 1)

ball = canvas.create_oval(10, 10, 30, 30, tags = 'ball') # create object to animate

def animation(x_move, y_move):
    canvas.move(ball, x_move, y_move) # movement
    canvas.update()
    canvas.after(20) # milliseconds in wait time, this is 50 fps

    tk.after_idle(animation, x_move, y_move) # loop variables and animation, these are updatable variables

animation(2, 2) # run animation

tk.mainloop()