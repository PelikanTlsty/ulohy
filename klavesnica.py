with open('chybyyz.txt', 'r') as file:
    obsah=file.read()
    
print(obsah)

print("Chyb v subore je: " +str( obsah.count("y")+obsah.count("z") ))

obsah=obsah.replace("y", "(placeHolder)")
obsah=obsah.replace("z", "y")
obsah=obsah.replace("(placeHolder)", "z")

with open('opravayz.txt', 'a') as file:
    file.write(obsah)
