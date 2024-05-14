from tkinter import *

root = Tk()

canvas = Canvas(root, width=500, height=500, bg="gray")
canvas.pack()



with open('spokojnost.txt', 'r') as file:
    print(file.read())

with open('spokojnost.txt', 'r') as file:
    obsah = file.readlines()


zoznam = []
for line in obsah:
    zoznam.append( line.strip() )




print("Pocet hlasujucich: " +str(len(zoznam)))
canvas.create_text(
    (250,50),
    text="Pocet hlasujucich: "  +str(len(zoznam)),
)


ano = 100/len(zoznam)*zoznam.count("ano")
print("Spokojni v %: " +str(ano))

canvas.create_rectangle(0, 300, ano, 350, fill="green")
canvas.create_text(
    (150,300),
    text = str(ano) + "%",
)


nie = 100/len(zoznam)*zoznam.count("nie")
print("Nespokojni v %: " +str(nie))

canvas.create_rectangle(0, 400, nie, 450, fill="red")
canvas.create_text(
    (150,400),
    text = str(nie) + "%",
)



with open('vysledky.txt', 'a') as file:
    file.write(
        "Pocet hlasujucich: " + str(len(zoznam)) + "\n"
        + "Ano v %: " +str(ano) + "\n"
        + "Nie v %: " +str(nie) + "\n"
    )


root.mainloop()