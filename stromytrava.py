import tkinter
import random
canvas=tkinter.Canvas(width=800,height=600)
canvas.pack()

x=random.randint(50,750)
y=random.randint(50,300)
z=random.randint(30,70)
p=random.randint(3,10)

def strom(x,y,z):
    canvas.create_rectangle(x-10,y,x+10,y+150,fill='saddle brown')
    canvas.create_oval(x-z,y-z,x+z,y+z,fill='light green')

for i in range(1,11):
    strom(x,y,z)
    x=random.randint(50,750)
    y=random.randint(50,300)
    z=random.randint(30,70)

def trava(x,y,p):
    for i in range(1,p):
        w=random.randint(1,3)
        a=random.randint(-20,20)
        b=random.randint(20,40)
        canvas.create_line(x,y,x+a,y-b,fill='green',width=w)

for i in range(1,21):
    trava(x,y,p)
    x=random.randint(50,750)
    y=random.randint(50,300)
    p=random.randint(3,10)

         
