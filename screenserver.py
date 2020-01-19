import tkinter
from random import randrange, randint

X_MAX, Y_MAX = 800, 600

canvas=tkinter.Canvas(width=X_MAX, height=Y_MAX, bg= 'white')
canvas.pack()

x = randint(0, X_MAX)
y = randint(0, Y_MAX)
r = 15
a = 2
b = 2


while True:
    canvas.delete('all')

    canvas.create_rectangle(x - r, y - r, x + r, y + r, fill = 'chocolate1', outline = 'chocolate1')

    x = x + a
    y = y + b

    if x > X_MAX - r or x <= r: 
        a = a * -1

    if y > Y_MAX - r or y <= r:
        b = b * -1
    
    canvas.update()
    canvas.after(5)
