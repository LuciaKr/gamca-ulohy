import tkinter
from random import randrange

X_MAX,Y_MAX= 400,400

canvas=tkinter.Canvas(width=X_MAX,height=Y_MAX, bg='white')
canvas.pack()

r = randrange(256)
g = randrange(256)
b = randrange(256)

xr = 1
xg = 1
xb = 1

while True:
    canvas.delete('all')
    farba= f"#{r:02x}{g:02x}{b:02x}"

    r=r+xr
    g=g+xg
    b=b+xb  

    canvas.create_rectangle(X_MAX-350,Y_MAX-350,X_MAX-50,Y_MAX-50,fill=farba)

    if r==0 or r==255:
        xr = xr * -1

    if g==0 or g==255:
        xg = xg * -1

    if b==0 or b==255:
        xb = xb * -1

    canvas.update()
    canvas.after(10)
