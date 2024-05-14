import random

n = int(input())

myList = []
for i in range(0,n):
    myList.append(random.randint(1,10))

print(myList)
print("Najvacsie cislo:" +str(max(myList)))
print("Priemerna hodnota: " +str(round(sum(myList)/len(myList),2)))

for i in range(1,10):
    print(str(i) +": " +str(myList.count(i)))

with open("losovanie.txt", "a") as file:
    for i in myList:
        file.write(str(i)+",")