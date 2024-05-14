from tkinter import *
import random
root = Tk()

canvas = Canvas(root, width=500, height=500, bg="gray")
canvas.pack()


speed=60
x=0
y=0
monochrome=False


def slowDown(event):
    global speed
    speed=speed+10
    
def speedUp(event):
    global speed
    if speed>10:
        speed=speed-10
def monochromeMode(event):
    global monochrome
    monochrome = True
def reset(event):
    canvas.create_rectangle(0,0,500,500,fill="gray")
    
root.bind("q", slowDown)
root.bind("e", speedUp)
root.bind("w", monochromeMode)
root.bind("<space>", reset)


def loop():
    global speed
    global x
    global y
    x=x+10
    y=y+10

    if x>500:
        x=0
        y=0
    
    if monochrome==False:
        red='#{:02x}{:02x}{:02x}'.format(random.randint(110,255),random.randint(0,1),random.randint(0,1))
        green='#{:02x}{:02x}{:02x}'.format(random.randint(0,1),random.randint(100,255),random.randint(0,1))
        blue='#{:02x}{:02x}{:02x}'.format(random.randint(0,1),random.randint(0,1),random.randint(100,255))

        canvas.create_line(x,0,0,500-y, fill=red)
        canvas.create_line(x,0,500,y, fill=green)
        canvas.create_line(500,y,500-y,500, fill=blue)
        canvas.create_line(500-x,500,0,500-y, fill=blue)
    else:
        shade=random.randint(10,50)
        gray='#{:02x}{:02x}{:02x}'.format(shade,shade,shade)

        canvas.create_line(x,0,0,500-y, fill=gray)
        canvas.create_line(x,0,500,y, fill=gray)
        canvas.create_line(500,y,500-y,500, fill=gray)
        canvas.create_line(500-x,500,0,500-y, fill=gray)


    root.after(speed,loop)
    
loop()

root.mainloop()
