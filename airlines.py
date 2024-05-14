with open("airlines.txt", "r") as file:
    lines=file.readlines()


letiska=[]

for i in range(len(lines)):
    lines[i]=lines[i].format()
    print(lines[i])
    letisko=lines[i].split(";") #Letisko z ktoreho lietaju linky
    letiska.append(letisko[0]) #Letiska z ktorych lietaju linky

print("____________________________________")

jednotliveLetiska=list(set(letiska))
pocetLiniek=[]

for i in jednotliveLetiska:
    print("Spolocnost prevadzkuje z letiska " +str(i)+ " " +str(letiska.count(i))+ " linku/linky/liniek:")
    pocetLiniek.append(int(letiska.count(i)))

print("____________________________________")

# create pairs
pairs = list(zip(jednotliveLetiska, pocetLiniek))

# extract first element and sort based on it
sorted_pairs = sorted(pairs, key=lambda x: x[1])

max_value = sorted_pairs[-1][1]
for i in sorted_pairs:
    if i[1] == max_value:
        print("Najvacsi pocet liniek ma letisko/ska: " +str(i[0]))

print("____________________________________")

for i in sorted_pairs:
    print(i)