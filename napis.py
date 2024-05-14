import time

slovo = str(input("Zadaj slovo: "))
i=0
text=""

def loop2():
    global i
    global text

    text=list(text)
    del(text[i])
    text=''.join(text)
    i=i-1
    print(text)
    
    if(0==len(text)):
        i=i+1
        time.sleep(1)
        loop()
        return
    
    time.sleep(1)
    loop2()

def loop():
    global i
    global text

    text=text+slovo[i]
    i=i+1
    print(text)
    if(len(slovo)==len(text)):
        i=i-1
        time.sleep(1)
        loop2()
        return

    time.sleep(1)
    loop()
loop()