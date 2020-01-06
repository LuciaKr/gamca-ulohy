import tkinter
from random import randrange, randint

X_MAX,Y_MAX=800,600

canvas=tkinter.Canvas(width=X_MAX,height=Y_MAX,bg="white")
canvas.pack()

a,b=0,0

def zaciatok(event):
    global a,b
    canvas.bind("<B1-Motion>",kreslenie)
    a,b=event.x,event.y

def kreslenie(event):
    x,y=event.x,event.y
    global a,b

    if a > X_MAX / 2 and b > Y_MAX /2:
        farba='sky blue'
    elif a > X_MAX / 2 and b <= Y_MAX /2:
        farba='pink'
    elif a <= X_MAX / 2 and b > Y_MAX /2:
        farba='light yellow'
    elif a <= X_MAX / 2 and b <= Y_MAX /2:
        farba='lavender'
    else:
        print ('RIP')
    
    canvas.create_line(a,b,x,y,width=5, fill=farba)
    a,b=x,y

canvas.bind("<Button-1>", zaciatok)
