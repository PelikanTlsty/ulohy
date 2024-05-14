from tkinter import *
import random

root = Tk()

canvas = Canvas(root, width=500, height=500, bg="gray")
canvas.pack()

xlistok=50*random.randint(0,7)
canvas.create_rectangle( xlistok, 400, xlistok+40, 420, fill="green" )
xlistok=xlistok+20

def drawPlates():
    for i in range(8):
        canvas.create_oval(i*50,400,i*50+40,440, fill="blue")
root.after(5000,drawPlates)

def click(event):
    global xlistok
    if (abs(event.x-xlistok)<20):
        if(abs(event.y-420)<20):
            print("Vyhra")
    else:
        if(event.x>xlistok):
            print("vlavo")
        else:
            print("vpravo")

canvas.bind("<Button-1>", click)


root.mainloop()