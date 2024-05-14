from tkinter import *
import random

root=Tk()

canvas=Canvas(root, width= 500, height = 500, background="gray")
canvas.pack()

blue=[]
yellow=[]
red=[]
stop = False

for i in range(8):
    id = canvas.create_line(i*60+40,500,i*60+40,500, fill="red", width=50)
    red.append(id)
    id = canvas.create_line(i*60+40,500,i*60+40,500, fill="yellow", width=50)
    yellow.append(id)  
    id = canvas.create_line(i*60+40,500,i*60+40,500, fill="blue", width=50)
    blue.append(id)  


def draw():
    global stop

    for i in range(len(blue)):
        height=random.randint(20,450)

        canvas.coords(red[i], i*60+40,500,i*60+40,500-height)
        if(height>350):
            height=350
        canvas.coords(yellow[i], i*60+40,500,i*60+40,500-height)
        if(height>200):
            height=200
        canvas.coords(blue[i], i*60+40,500,i*60+40,500-height)

    if(stop==False):
        root.after(1000,draw)
draw()

def stopOnSpace(event):
    global stop
    stop = True
root.bind("<space>", stopOnSpace)

root.mainloop()