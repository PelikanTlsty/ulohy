from tkinter import *

root=Tk()

canvas=Canvas(root,width=500,height=500, background="gray")
canvas.pack()

pixely=0
jednotky=0


with open("preklopenie_obrazka.txt", "r") as file:
    lines=file.readlines()

for i in range(len(lines)):
    lines[i]=lines[i].replace(" ", "")


def draw():
    canvas.create_rectangle(0,0,500,500,fill="gray")
    global pixely
    global jednotky

    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if(lines[y][x] == "0"):
                canvas.create_rectangle(x*10,y*10,x*10+10,y*10+10, fill="white")
            
            if(lines[y][x] == "1"):
                canvas.create_rectangle(x*10,y*10,x*10+10,y*10+10, fill="black")
                jednotky=jednotky+1

            pixely=pixely+1
draw()

print("Pixelov: " +str(pixely))
print("Jednotiek: " +str(jednotky))


def flip():
    for i in range(len(lines)):
        lines[i]=lines[i][::-1]
    draw()
b=Button(text="preklopit", command=flip)
b.pack(pady=20)

root.mainloop()