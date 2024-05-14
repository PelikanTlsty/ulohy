from tkinter import *
import random

colors = ["red", "green", "yellow", "blue", "pink"]

def draw(event):
    canvas.create_oval(event.x, event.y, event.x+50, event.y+50, fill=colors[random.randint(0,4)])

    with open('kreslenie.txt', 'a') as file:
        file.write(str(event.x) +"\n")
        file.write(str(event.y) +"\n")


def erase(event):
    canvas.create_rectangle(0,0,500,500, fill="gray")

    with open('kreslenie.txt', 'w') as file:
        file.write("")


root = Tk()

canvas = Canvas(root, width=500, height=500, background="gray")
canvas.pack()


root.bind('<Button-1>', draw)
root.bind('<space>', erase)


root.mainloop()
