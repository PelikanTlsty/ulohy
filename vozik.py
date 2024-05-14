from tkinter import *
import random
root = Tk()

canvas = Canvas(root, width=500, height=500, bg="gray")
canvas.pack()

back=False

vozik = canvas.create_rectangle(100,450,200,400, fill="blue")
koleso1 = canvas.create_oval(80,480,120,440, fill="yellow")
koleso2 = canvas.create_oval(80+100,480,120+100,440,fill="yellow")

def reset(event):
    canvas.coords(vozik, 100,450,200,400)
    canvas.coords(koleso1, 80,480,120,440)
    canvas.coords(koleso2, 80+100,480,120+100,440)
    canvas.itemconfig(vozik, fill="blue")
    global back
    back=False

def loop():
    global back
    if (canvas.coords(vozik)[0]>400):
        back=True
        canvas.itemconfig(vozik, fill="red")
    if (canvas.coords(vozik)[0]<0):
        back=False
        canvas.itemconfig(vozik, fill="blue")

    if (back==True):
        canvas.move(vozik,-5,0)
        canvas.move(koleso1,-5,0)
        canvas.move(koleso2,-5,0)
    else:
        canvas.move(vozik,5,0)
        canvas.move(koleso1,5,0)
        canvas.move(koleso2,5,0)


    root.after(60,loop)
loop()

root.bind("<space>", reset)

root.mainloop()
