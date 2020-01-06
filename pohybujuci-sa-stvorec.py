import tkinter
from random import randrange, randint

X_MAX, Y_MAX = 800, 600

#a, b = 55,88
#a, b = b, a

canvas=tkinter.Canvas(width=X_MAX, height=Y_MAX, bg= 'white')
canvas.pack()

#for _ in range(100000):
    #x,y = randrange(X_MAX), randrange(Y_MAX)

    #if (y > Y_MAX/2):
        #farba = 'deep sky blue'
    #else:
        #farba = 'light coral'
    #canvas.create_rectangle(x-5,y-5,x+5,y+5, fill=farba)

#tkinter.mainloop()

r=50
x,y = randrange(X_MAX-r), r + randrange(Y_MAX - 2*r)
dx = 1


while True:
    canvas.delete('all')

    canvas.create_rectangle(x-10,y-10,x+10,y+10, fill='chocolate1')

    x += dx

    if x == X_MAX -r :
        dx = -1

    if x == r:
        dx = 1
    
    canvas.update()
    canvas.after(1)
