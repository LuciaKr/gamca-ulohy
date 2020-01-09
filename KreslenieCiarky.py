import tkinter
from random import randrange, randint

X_MAX,Y_MAX=800,600
xx,yy=0,0

canvas=tkinter.Canvas(width=X_MAX,height=Y_MAX,bg="white")
canvas.pack()

def kliknutie(event):
    global xx,yy
    canvas.bind("<B1-Motion>",ciarka)
    xx,yy=event.x,event.y


def ciarka(event):
    global xx,yy
    x,y=event.x,event.y
    canvas.create_line(xx,yy,x,y,width=4, fill='sky blue')
    xx,yy=x,y

canvas.bind("<Button-1>", kliknutie)
