import Tkinter as tk
import threading
import time
from threading import Thread
from Tkinter import *

light1 = False

def changeLight():
    global light1
    light1 = not light1

root=tk.Tk()
root.title("Traffic Simulation")
button = tk.Button(root, text='Stop', width=25, command=changeLight)
button.pack()
SIZE = 600

canvas = tk.Canvas(root, width = SIZE, height = SIZE, bg = "#FFE19C")
canvas.pack()

# generate the map
intersection_data = [
    (0,200,SIZE,200),
    (0,300,SIZE,300),
    (0,400,SIZE,400),
    (200,0,200,SIZE),
    (300,0,300,SIZE),
    (400,0,400,SIZE)
]

for t in intersection_data:
    # canvas.create_line(x0, y0, x1, y1, ..., xn, yn, option, ...)
    canvas.create_line(t, width = 5)

class Light(Thread, object):
    def __init__():
        Thread.__init__(self)

class Car(Thread, object):
    def __init__(self, a,b,c,d, outline='blue', fill='blue'):
        Thread.__init__(self)
        self.rect = canvas.create_rectangle(a,b,c,d, outline=outline, fill=fill)
        self.speed = (0, 0)
    def move(self):
        if(light1):
            canvas.move(self.rect, self.speed[0], self.speed[1])
    def set_speed(self, x, y):
        self.speed = x, y

car1 = Car(100, 100, 105, 105, outline='blue', fill='blue')
car1.set_speed(5, 0)
car2 = Car(20, 180, 40, 195, outline='red', fill = 'red')
car2.set_speed(3, 0)

# move cars
for x in range(2000):
    time.sleep(0.025)
    car1.move()
    car2.move()
    canvas.update()

# start the Simulation
root.mainloop()
