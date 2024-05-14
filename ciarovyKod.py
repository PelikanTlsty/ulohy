from tkinter import *
import random

root = Tk()

canvas = Canvas(root, width=500, height=500, bg="gray")
canvas.pack()

for i in range(1,random.randint(10,20)):
    x=i*15
    w=random.randint(0,9)
    canvas.create_line(x,100,x,200,width=w)
    print(i)
    canvas.create_text(
        (x,220),
        text=str(w)
    )
root.mainloop()
