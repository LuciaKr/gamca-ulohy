import tkinter
from random import randrange, randint

X_MAX, Y_MAX = 800, 600

canvas=tkinter.Canvas(width=X_MAX, height=Y_MAX, bg= 'white')
canvas.pack()


r=50
x,y = randrange(X_MAX-r), r + randrange(Y_MAX - 2*r)

for i in range(10000):
    x,y = randrange(X_MAX), randrange(Y_MAX)

    if x <= X_MAX/5 and y <= Y_MAX/4:
        farba='yellow'

    elif x <= X_MAX/5 and y <= Y_MAX/8:
        farba='blue'

    canvas.create_rectangle(x-5,y-5,x+5,y+5, fill=farba)
