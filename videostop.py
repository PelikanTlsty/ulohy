from tkinter import *
import random

root= Tk()

canvas = Canvas(root, width=200, height=100, background="gray")
canvas.pack()

spravne = 0
vsetky = 0

colors = ["red","blue","green","yellow","pink" ]


def stop(): #Najprv loop vytvara farby
    global farba1
    global farba2
    global spravne
    global vsetky

    vsetky = vsetky+1

    if (farba1==farba2):
        print("Vyhra")
        spravne = spravne+1

    label.config(text="Spravne " +str(spravne) +" z "+ str(vsetky))
        

b=Button(text="Stop", command=stop)
b.pack(pady=20)

label=Label(text="Spravne " +str(spravne) +" z "+ str(vsetky))
label.pack(pady=20)


def loop():
    global farba1
    global farba2
    farba1=random.randint(0,4)
    farba2=random.randint(0,4)

    canvas.create_rectangle(0,0,100,100, fill=colors[farba1])
    canvas.create_rectangle(200,0,100,100, fill=colors[farba2])
    
    root.after(300,loop)
loop()

root.mainloop()