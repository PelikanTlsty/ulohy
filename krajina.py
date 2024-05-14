from tkinter import *
import random

colors = ["green", "limeGreen", "lawnGreen", "lime", "lightGreen"]

def draw(event):
    canvas.create_rectangle(0,0,500,500, fill = "gray")
    for i in range(0,6):
        vrchol = random.randint(100,300)
        coords=[-300+i*50,500]

        x=-300+i*50
        y=0

        while y<vrchol:
            y=y+random.randint(0,10)
            x=x+10
            coords.append(x)
            coords.append(500-y)
        while y>0:
            y=y-random.randint(0,10)
            x=x+10
            coords.append(x)
            coords.append(500-y)

        canvas.create_polygon(coords, 500, 500, fill=colors[random.randint(0,3)], outline="black")



root = Tk()

canvas = Canvas(root, width=500, height=500, background="gray")
canvas.pack()


root.bind('<space>', draw)
draw("0")

root.mainloop()
