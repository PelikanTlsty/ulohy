from tkinter import *
import random

root=Tk()
canvas=Canvas(root,width=500,height=500,background="gray")
canvas.pack()

ids=[]
selected=[]


for i in range(30):
    x=random.randint(0,500)
    y=random.randint(0,500)
    id=canvas.create_oval(
        0+x,
        0+y,

        10+x,
        10+y,
        fill="green"
    )
    ids.append(id)
for i in range(30):
    x=random.randint(0,500)
    y=random.randint(0,500)
    id=canvas.create_oval(
        0+x,
        0+y,

        10+x,
        10+y,
        fill="yellow"
    )
    ids.append(id)



def click(event):
    global selected
    global oldPos

    if(selected==[]):
        selected=[]
        oldPos=[]
        for i in ids:
            if(abs(canvas.coords(i)[0]-event.x)<30 and abs(canvas.coords(i)[1]-event.y)<30):
                selected.append(i)
                oldPos.append((canvas.coords(i)[0],canvas.coords(i)[1]))

        oldPos.append((event.x, event.y)) #store mouse pos as last element
    else:
        selected=[]
        oldPos=[]
canvas.bind("<Button-1>", click)

def motion(event):
    global selected
    global oldPos
    
    for i in range(len(selected)):
        x=oldPos[i][0]-oldPos[-1][0]
        y=oldPos[i][1]-oldPos[-1][1]

        canvas.coords(selected[i], x+event.x, y+event.y, x+event.x+10, y+event.y+10)

canvas.bind("<Motion>", motion)


def loop():
    for i in ids[0:30]:
        for j in ids[30:60]:
            if(i != j):
                if(abs(canvas.coords(i)[0]-canvas.coords(j)[0])<100 and abs(canvas.coords(i)[1]-canvas.coords(j)[1])<100):
                    root.after(100,loop)
                    return

    print("Vyhral si!")
loop()
    

root.mainloop()