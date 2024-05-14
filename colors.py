from tkinter import *
import random

inp = input("Zadaj reklamu: ")
inp = list(inp)
pismena = []

colors=[ "yellow", "red", "green", "orange", "blue", "pink"]

root = Tk()
canvas = Canvas( root, width=500, height=500, background="gray")
canvas.pack()

print(inp)

for i in range(len(inp)):
    id=canvas.create_text(
        (10+i*20,250),
        text=inp[i],
        font=("Arial", 20)
    )
    pismena.append(id)


def changeColor():
    for i in pismena:
        canvas.itemconfig(i, fill=colors[random.randint(0,5)])
    root.after(1000, changeColor)
changeColor()

root.mainloop()