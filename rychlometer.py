from tkinter import *

root = Tk()

canvas = Canvas(root, width=200, height=500, bg="black")
canvas.pack()

for i in range(0,20):
    canvas.create_text(
        (50,i*20),
        text=str(i*10)+" _____",
        fill="white"
    )

speed = 0
def rychlejsie():
    global speed
    if(speed<130):
        speed = speed +5
        canvas.create_rectangle(100,0,200,500,fill="black")
        canvas.create_rectangle(100,0,150,speed*2,fill="red")
def pomalsie():
    global speed
    speed = speed -5
    canvas.create_rectangle(100,0,200,500,fill="black")
    canvas.create_rectangle(100,0,150,speed*2,fill="red")

r=Button(text="Rychlejsie", command=rychlejsie)
r.pack(pady=20)
p=Button(text="Pomalsie", command=pomalsie)
p.pack(pady=20)



root.mainloop()