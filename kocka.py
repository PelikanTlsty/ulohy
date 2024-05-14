from tkinter import *
import random

root = Tk()

canvas = Canvas(root, width=500, height=500, bg="gray")
canvas.pack()


hody = []

for i in range(1,1001):
    cislo = random.randint(1,6)
    hody.append( cislo )
    print("Pri hode " +str(i)+ " padlo cislo " +str(cislo))


    with open('hody.txt', 'a') as file:
        file.write(str(cislo) + "2\n")
    

print( "Cislo 1 padlo " +str(hody.count(1))+ "-krat." )
print( "Cislo 2 padlo " +str(hody.count(2))+ "-krat." )
print( "Cislo 3 padlo " +str(hody.count(3))+ "-krat." )
print( "Cislo 4 padlo " +str(hody.count(4))+ "-krat." )
print( "Cislo 5 padlo " +str(hody.count(5))+ "-krat." )
print( "Cislo 6 padlo " +str(hody.count(6))+ "-krat." )


canvas.create_rectangle(10, 500, 50, hody.count(1), fill="blue")
canvas.create_text(
    (25, 400),
    text="1"
)
canvas.create_rectangle(60, 500, 100, hody.count(2), fill="red")
canvas.create_text(
    (75, 400),
    text="2"
)
canvas.create_rectangle(110, 500, 150, hody.count(3), fill="green")
canvas.create_text(
    (125, 400),
    text="3"
)
canvas.create_rectangle(160, 500, 200, hody.count(4), fill="pink")
canvas.create_text(
    (175, 400),
    text="4"
)
canvas.create_rectangle(210, 500, 250, hody.count(4), fill="orange")
canvas.create_text(
    (225, 400),
    text="5"
)

canvas.create_rectangle(260, 500, 300, hody.count(4), fill="yellow")
canvas.create_text(
    (275, 400),
    text="6"
)



root.mainloop()
