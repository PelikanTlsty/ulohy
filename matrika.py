from tkinter import *


def spracuj(arg):
    text = entry.get()
    text=text.replace(".", "")
    text=text.replace(" ", "")
    
    if(arg==0):
        rodne = text[6:8] +text[2:4] +text[0:2] +"/" +text[8:12]
        test = int(text[6:8] +text[2:4] +text[0:2] +text[8:12])
    elif(arg==50):
        rodne = text[6:8] +str(int(text[2:4])+50) +text[0:2] +"/" +text[8:12]
        test = int(text[6:8] +str(int(text[2:4])+50) +text[0:2] +text[8:12])

    if(test % 11 == 0):
        with open('spravne_rodne_cisla.txt', 'a') as file:
            file.write(rodne +"\n")
    else:
        with open('vadne_rodne_cisla.txt', 'a') as file:
            file.write(rodne +"\n")

root = Tk()
root.geometry("300x200")

entry = Entry(root)
entry.pack(pady=20)

muz = Button(root, text="Zapisat muza", command = lambda:spracuj(0))
muz.pack(pady=20)
zena = Button(root, text="Zapisat zenu", command = lambda:spracuj(50))
zena.pack(pady=10)

root.mainloop()
