from tkinter import *
import random

root=Tk()

canvas=Canvas(root, width=500, height=500, background="gray")
canvas.pack()


coords=(random.randint(100,400), random.randint(100,400))
canvas.create_text(
    (coords[0],coords[1]),
    text="%",
    fill="red",
    font=("Arial", 50)
)

def draw():
    for i in range(30):
        canvas.create_line(i*20, 0, i*20, 500, width=15,fill="brown")

    canvas.create_line(0, 100, 500, 100, width=15,fill="brown")
    canvas.create_line(0, 400, 500, 400, width=15,fill="brown")
root.after(100, draw)



def click(event):
    global coords
    mouse=(event.x,event.y)

    if(abs(coords[0]-mouse[0])<50 and abs(coords[1]-mouse[1])<50):
        print("Vyhral si")
        
    elif(coords[0]-mouse[0]>0):
        print("Vpravo")
    elif(coords[0]-mouse[0]<0):
        print("Vlavo")


root.bind("<Button-1>", click)


root.mainloop()