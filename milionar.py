from tkinter import *

root = Tk()
root.geometry("300x200")

entry = Entry(root)
entry.pack(pady=20)

display = Text(root, height=10, width=25, bg="light yellow")
display.pack(pady=20)

def loop():
    suma = entry.get()
    nasetrene = suma
    roky=0

    while (nasetrene<1000000):
        nasetrene=nasetrene+(nasetrene/100*15)
        roky=roky+1

    display.delete("1.0", END)
    display.insert("1.0", roky)


    root.after(1000, loop)
loop()

root.mainloop()
