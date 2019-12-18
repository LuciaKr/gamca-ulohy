import tkinter
import random

X_MAX, Y_MAX = 800,600

canvas=tkinter.Canvas(width=X_MAX, height=Y_MAX, bg='white')
canvas.pack()

def klik(event):
    x,y = event.x, event.y
    r=10
    canvas.create_oval(x,y,x+10,y+10, fill='black')
    
def pohyb(event):
    x,y = event.x, event.y
    r=10
    canvas.create_oval(x,y,x+10,y+10, fill='pink')

canvas.bind('<Button-1>', klik)
canvas.bind('<Motion>', pohyb)
