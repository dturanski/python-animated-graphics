from graphics import *

graphics = Graphics(800, 500)

car = Group(graphics)

car.add(graphics.rectangle((20, 370), (200, 450), fill='purple'))

car.add(graphics.rectangle((55, 305), (170, 370), fill='purple'))

car.add(graphics.circle((60, 450), 25, fill='black'))

car.add(graphics.circle((160, 450), 25, fill='black'))

car.add(graphics.rectangle((60, 310), (110, 360), fill='white'))

car.add(graphics.rectangle((115, 310), (165, 360), fill='white'))

for i in range(120):
    car.move((5, 0))

for i in range(120):
    car.move((-5, 0))

for i in range(60):
    car.move((0, -5))

for i in range(60):
    car.move((0, 5))

graphics.show()