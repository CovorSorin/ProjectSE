import Tkinter as tk
import threading
import time
from threading import Thread
from Tkinter import *

light1 = True
light2 = False

def changeLights():
    global light1
    global light2
    light1 = not light1
    light2 = not light2

root = tk.Tk()
root.title("Traffic Simulation")
button = tk.Button(root, text = 'Change Lights', width = 25, command = changeLights)
button.pack()

# window size
# lane_width(px) = WIDTH
WIDTH = 60
SIZE = 10 * WIDTH

canvas = tk.Canvas(root, width = SIZE, height = SIZE, bg = "#FFE19C")
canvas.pack()

# draw the intersection on the screen
# canvas.create_line(x0, y0, x1, y1, ..., xn, yn, option, ...)

intersection_colors = [
    (0, 6 * WIDTH, SIZE, WIDTH * 4),
    (6 * WIDTH, 0, WIDTH * 4, SIZE)
]

for t in intersection_colors:
    canvas.create_rectangle(t, fill = "#999999", outline = '#999999')

intersection_data = [
    (0, 4 * WIDTH, SIZE, 4 * WIDTH),
    (0, 6 * WIDTH, SIZE, 6 * WIDTH),
    (4 * WIDTH, 0, 4 * WIDTH, SIZE),
    (6 * WIDTH, 0, 6 * WIDTH, SIZE)
]

for t in intersection_data:
    canvas.create_line(t, width = 5)

intersection_lines = [
    (0, 5 * WIDTH, SIZE, 5 * WIDTH),
    (5 * WIDTH, 0, 5 * WIDTH, SIZE)
]

for t in intersection_lines:
    canvas.create_line(t, width = 5, fill = "White")

padding = 10
class Car(Thread, object):
    def __init__(self, spawn, outline = 'blue', fill = 'blue'):
        Thread.__init__(self)
        self.pos = self.getPos(spawn)
        self._x = 0
        self._y = 0
        self.rect = canvas.create_rectangle(self.pos, outline = outline, fill = fill)
        self.speed = (0, 0)
    def move(self):
        #print canvas.coords(self.rect)
        if(light1):
            canvas.move(self.rect, self.speed[0], self.speed[1])
            self._x += self.speed[0]
            self._y += self.speed[1]
        else:
            if(abs(self._x) < 3 * WIDTH):
                # print self._x
                canvas.move(self.rect, self.speed[0], self.speed[1])
                self._x += self.speed[0]
                self._y += self.speed[1]
    def set_speed(self, x, y):
        self.speed = x, y
    def getPos(self, spawn):
        if (spawn == 1):
            a = 0
            b = 5 * WIDTH + padding
            c = WIDTH
            d = 6 * WIDTH - padding
            self._x = a
            self._y = b
            return (a, b, c, d)
        if (spawn == 2):
            a = SIZE
            b = 4 * WIDTH + padding
            c = 9 * WIDTH
            d = 5 * WIDTH - padding
            self._x = a
            self._y = b
            return (a, b, c, d)

car1 = Car(1, outline = 'blue', fill = 'blue')
car1.set_speed(2, 0)
car2 = Car(2, outline = 'red', fill = 'red')
car2.set_speed(-2, 0)

# move cars
for x in range(5000):
    time.sleep(0.025)
    car1.move()
    car2.move()
    canvas.update()

# start the Simulation
root.mainloop()
