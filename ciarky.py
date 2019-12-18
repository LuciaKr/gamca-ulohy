import tkinter
from random import randrange, randint

X_MAX, Y_MAX = 800, 600

canvas=tkinter.Canvas(width=X_MAX, height=Y_MAX, bg= 'white')
canvas.pack()

x,y = 400,300

for i in range(1000):
    a = randint (-1000,1000)
    b = randint(-1000,1000)

    
    if (x + a) > X_MAX/2 and (y + b) > Y_MAX/2:
        farba='sky blue'
    elif (x + a) > X_MAX/2 and (y + b) <= Y_MAX/2:
        farba='pink'
    elif (x + a) <= X_MAX/2 and (y + b) <= Y_MAX/2:
        farba='yellow'
    elif (x + a) <= X_MAX/2 and (y + b) > Y_MAX/2:
        farba='green'
    else:
        print('RIP')
    
    canvas.create_line(x,y,x+a,y+b, fill=farba)
    
    
