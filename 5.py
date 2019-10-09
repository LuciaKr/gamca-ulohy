import tkinter
import random
canvas=tkinter.Canvas(width=800, height=600)
canvas.pack()

def dom(x,y,z):
    canvas.create_rectangle(x,y,x+z,y+z, outline='blue', fill='blue')
    canvas.create_polygon(x,y, x+1/2*z,y-1/2*z, x+z,y, fill='red')

x=random.randint(50,600)
y=random.randint(100,600)
z=30

for i in range(1,4):
    x=x+2*z
    dom(x,y,z)
