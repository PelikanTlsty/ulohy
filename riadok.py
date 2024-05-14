with open('dlhyriadok.txt', 'r') as file:
    obsah=file.read()

dlzka=int(input("Dlzka riadku:"))+1
originalDlzka=dlzka

while dlzka<len(obsah):
    obsah = obsah[:dlzka-1] + "\n" + obsah[dlzka-1:]
    dlzka = dlzka + originalDlzka

print(obsah)

with open('zapis.txt', 'a') as file:
    file.write(obsah)