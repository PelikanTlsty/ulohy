vklad = input("Zadaj sumu:")

if(vklad[-1] != "0"):
    print("Suma sa neda vyplatit")
else:

    vklad=int(vklad)

    stovky = int(vklad/100)
    print("stovky: " +str(stovky))
    ostatok = vklad % 100

    patdesiatky = int(ostatok/50)
    print("patdesiatky: " +str(patdesiatky))
    ostatok = ostatok % 50

    dvadsiatky = int(ostatok/20)
    print("dvadsiatky: " +str(dvadsiatky))
    ostatok = ostatok % 20

    desiny = int(ostatok/10)
    print("Desiny: " +str(desiny))