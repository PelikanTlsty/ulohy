from tkinter import *
import random

root=Tk()

canvas=Canvas(root, width=500, height=500, background="darkGreen")
canvas.pack()


cesta=[]
offset=0
move=0

for i in range(55):
    cesta.append(250)
    
def loop():
    global offset
    global move

    offset=offset+10*random.randint(0,1)-10*random.randint(0,1)
    cesta.insert(0,250+offset)

    canvas.delete("all")

    for y in range(len(cesta)):
        canvas.create_rectangle(
                                cesta[y]-30+move,
                                y*10,
                                cesta[y]+30+move,
                                y*10+10,
        fill="gray")
    
    canvas.create_rectangle(240,450,260,430,fill="red")

    root.after(100,loop)
loop()

def left(event):
    global move
    move=move+5
root.bind("<Left>", left)
def right(event):
    global move
    move=move-5
root.bind("<Right>", right)

root.mainloop()