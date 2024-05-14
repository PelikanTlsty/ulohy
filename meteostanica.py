with open("meteostanice.txt", "r") as file:
    lines=file.readlines()

print("pocet merani: " +str(len(lines)))

extrakcia=[]
priemer=0
for i in lines:
    i=i.strip()
    i=i.replace(",", ".")

    print(i[21:26])
    extrakcia.append((i[0:3], float(i[21:26])))
    priemer=priemer+float(i[21:26])


extrakcia=sorted(extrakcia, key=lambda x: x[1])
print("Kod stanice a jej teplota (najvyssia zo vsetkych):" +str(extrakcia[-1]))

print("Priemerna hodnota: " +str(priemer/len(extrakcia)))