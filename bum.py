from tkinter import *
import random

root = Tk()

canvas = Canvas(root, width=500, height=500, bg="gray")
canvas.pack()

blue=canvas.create_oval(0,400,50,450, fill="blue")
red=canvas.create_oval(500,400,550,450, fill="red")

def loop():
    canvas.move(blue, random.randint(5,10), 0)
    canvas.move(red, -random.randint(5,10), 0)

    coordsBlue=canvas.coords(blue)
    coordsRed=canvas.coords(red)

    if(coordsBlue[0]<coordsRed[0]):
        root.after(60,loop)
    else:
        canvas.create_text(
            (coordsBlue[0],380),
            text="BUM"
        )
loop()

root.mainloop()
