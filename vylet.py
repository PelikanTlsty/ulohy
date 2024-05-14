with open('prihlaseni.txt', 'r') as file:
    print(file.read())

with open('prihlaseni.txt', 'r') as file:
    obsah = file.readlines()


zoznam = []
for line in obsah:
    zoznam.append( line.strip() )

ludia = list(zoznam)
del ludia[2-1::2]
print("Pocet prihlasenych: " +str(len(ludia)) )



vek = list(zoznam)
del vek[1-1::2]

priemernyVek = 0
for i in vek:
    priemernyVek = priemernyVek + int(i)

print("Priemerny vek: " +str(priemernyVek/len(vek)) )



counter=0
for i in range(0,len(ludia)):
    if( int(vek[i]) < 15 ):
        counter=counter+1

print("Pocet osob mladsich ako 15: " +str(counter) )




cena = input("Zadaj cenu pre 1 osobu:")
spolu = int(cena)*len(ludia) - counter*int(cena)*0.5
print("Cena spolu: " +str(spolu))