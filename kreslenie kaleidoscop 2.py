import tkinter
import random

X_MAX, Y_MAX = 800,600

canvas=tkinter.Canvas(width=X_MAX, height=Y_MAX, bg='white')
canvas.pack()
    
def pohyb(event):
    x,y = event.x, event.y
    r=20
    canvas.create_oval(x,y,x+r,y+r, fill='lavender')
    a= X_MAX - x
    canvas.create_oval(a-r,y-r,a,y, fill='sky blue')
    b= Y_MAX - y
    canvas.create_oval(x-r,b-r,x,b, fill='light yellow')
    
    

canvas.bind('<Motion>', pohyb)

#pink