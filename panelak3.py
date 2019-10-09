import tkinter
import random
canvas=tkinter.Canvas(width=800, height=600)
canvas.pack()

a=random.randint(0,50)

def panelak(x,y,s,v):
    canvas.create_rectangle(x,y,x+10+s*20,y+10+v*20,  fill='yellow')
    z=y
    for i in range(s):
        for j in range(v):
            canvas.create_rectangle(x+10,y+10,x+20,y+20, fill='light blue')
            y=y+20
        y=z
        x=x+20
        


def mesto():
    for i in range(1,a):
      
        panelak(random.randint(0,700),random.randint(0,500), random.randint(2,5),random.randint(3,10))
mesto()
