import Tkinter as tk
import time

root=tk.Tk()
root.title("Traffic Simulation")

WIDTH = 500
HEIGHT = 500
canvas = tk.Canvas(root, width = WIDTH, height = HEIGHT, bg = "#FFE19C")
canvas.pack()

# generate the map
intersection_data = [
    (0,300,500,300),
    (0,200,500,200),
    (300,0,300,500),
    (200,0,200,500)
]

for t in intersection_data:
    # canvas.create_line(x0, y0, x1, y1, ..., xn, yn, option, ...)
    canvas.create_line(t, width = 5)

# start the Simulation
root.mainloop()
