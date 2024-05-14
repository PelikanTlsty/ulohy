from tkinter import *

root=Tk()

canvas=Canvas(root,width=500,height=500,background="lightYellow")
canvas.pack()

squares=[]
for i in range(1,24):
    id=canvas.create_rectangle(i*20,200,i*20+20,220, fill="white")
    squares.append(id)

def on_motion(event):
    futureItem=None
    for i in squares:
        canvas.itemconfig(i,fill="white")
        if(abs(event.y-210)<10):
            if(abs(canvas.coords(i)[0]+10-event.x)<10):
                futureItem=i #buggg
                canvas.itemconfig(i,fill="black")
                if(i>0):
                    canvas.itemconfig(i-1,fill="gray")

            if(i-1==futureItem):
                canvas.itemconfig(i,fill="gray")
    
            





canvas.bind("<Motion>", on_motion)

root.mainloop()