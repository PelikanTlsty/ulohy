from tkinter import *
import random

root=Tk()
canvas=Canvas(root,width=500,height=500,background="gray")
canvas.pack()
grass=[]
for i in range(1,50):
    color = '#{:02x}{:02x}{:02x}'.format(0,random.randint(100,255),0)
    id=canvas.create_rectangle(i*10,500,i*10+10,500-random.randint(50,100), fill=color)
    grass.append(id)


def pokosit():
    for i in grass:
        canvas.coords(i, i*10,500,i*10+10,450)

pok=Button(text="pokosit", command=pokosit)
pok.pack(pady=10)

def poliat():
    for i in grass:
        canvas.coords(i, i*10,500,i*10+10,canvas.coords(i)[1]-random.randint(0,20))
        print(canvas.coords(i))

pol=Button(text="poliat", command=poliat)
pol.pack(pady=10)



root.mainloop()