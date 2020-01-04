import tkinter
from random import randrange, randint

X_MAX, Y_MAX = 800, 600

canvas=tkinter.Canvas(width=X_MAX, height=Y_MAX, bg= 'white')
canvas.pack()


r=5

for i in range(10000):
    x,y = randrange(X_MAX), randrange(Y_MAX)

    if x <= X_MAX/(8/3) and y <= Y_MAX/(12/5) or x <= X_MAX/(8/3) and y > Y_MAX/(12/7) or \
       x > X_MAX/2 and y <= Y_MAX/(12/5) or x > X_MAX/2 and y > Y_MAX/(12/7) :
        farba='blue'

    else:
        farba= 'yellow'

    canvas.create_rectangle(x-r,y-r,x+r,y+r, fill=farba)
