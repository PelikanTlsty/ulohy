from tkinter import *
import random


root=Tk()

canvas=Canvas(root, width=500,height=500, background="gray")
canvas.pack()



color="brown"
for y in range(1,11):
    for x in range(1,11):
        canvas.create_text(
            (x*45,y*45),
            text=x*y,
            fill=color,
            font=("Arial", 15)
        )
    if(color=="brown"):
        color="blue"
    elif(color=="blue"):
        color="brown"



def novyPriklad():
    global a
    global b

    a=random.randint(1,10)
    b=random.randint(1,10)

    label.config(text=str(a)+"*"+str(b))

button=Button(text="novy priklad", command=novyPriklad)
button.pack(pady=10)


label=Label(text="Klikni na tlacidlo novy priklad")
label.pack(pady=10)


entry=Entry()
entry.pack(pady=10)


def vyhodnot():
    global a
    global b
    
    if(int(entry.get())==a*b):
        label2.config(text="Spravne")
    else:
        label2.config(text="Nespravne")

ok=Button(text="OK", command=vyhodnot)
ok.pack() 

label2=Label(text="EEE")
label2.pack(pady=20)

root.mainloop()