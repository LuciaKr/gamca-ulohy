import tkinter
from random import randrange, randint

X_MAX, Y_MAX = 800, 600

canvas=tkinter.Canvas(width=X_MAX, height=Y_MAX, bg= 'white')
canvas.pack()

r=50
x,y = randrange(X_MAX-r), r + randrange(Y_MAX - 2*r)


for _ in range(100000):

    x,y = randrange(X_MAX), randrange(Y_MAX)

    if x > X_MAX / 2 and y > Y_MAX /2:
        farba='blue'
    elif x > X_MAX / 2 and y <= Y_MAX /2:
        farba='light blue'
    elif x <= X_MAX / 2 and y > Y_MAX /2:
        farba='dark blue'
    elif x <= X_MAX / 2 and y <= Y_MAX /2:
        farba='sky blue'
    else:
        print ('RIP')

    canvas.create_rectangle(x-5,y-5,x+5,y+5, fill=farba)
