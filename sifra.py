from tkinter import *

abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","v","z","a","b","c"]


root = Tk()
root.geometry("300x200")


entry = Entry(root)
entry.pack(pady=20)

display = Text(root, height=10, width=25, bg="light yellow")
display.pack(pady=20)

def loop():
    text = entry.get()

    sifra=""
    for i in text:
        if i == " ":
            sifra = sifra + " "
        else:
            index=abc.index(i)
            sifra=sifra+abc[index+3]

    display.delete("1.0", END)
    display.insert("1.0", sifra)

    with open('sifra.txt', 'w') as file:
        file.write(sifra)

    root.after(1000, loop)
loop()

root.mainloop()
