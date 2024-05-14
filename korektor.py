with open("clanok.txt", "r") as file:
    obsah = file.read()

print("V texte je " +str(len(obsah))+ " znakov vratane medzier.")



obsah=list(obsah)
obsah[0]=obsah[0].upper()
obsah.insert(0,"X")
obsah.insert(0,"X")

for i in range(1,len(obsah)):
    if(obsah[i-2]=="." or obsah[i-2]=="?" or obsah[i-2]=="!"):
        obsah[i]=obsah[i].upper()

del obsah[0:2] 
obsah="".join(obsah)



samohlasky=["a", "e", "i", "o", "u"]
pocetSamohlasok=0
for i in samohlasky:
    obsah.count(i)
    pocetSamohlasok=pocetSamohlasok+obsah.count(i)
print("V texte je " +str(pocetSamohlasok)+ " samohlasok.")



with open("clanok_novy.txt", "a") as file:
    file.write(obsah)



