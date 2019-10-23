import tkinter
import random
canvas=tkinter.Canvas(width=800, height=600, bg='white')
canvas.pack()

def lodka(a,b, c, d):
    canvas.create_rectangle(a+d*7/3*c,b-d*13/3*c,a+d*8/3*c,b+d, outline='brown', fill='brown')
    canvas.create_polygon(a+d,b+d,a+d*c,b+d*2*c,a+d*4*c,b+d*2*c,a+d*5*c,b+d, outline='black', fill='saddle brown')
    canvas.create_polygon(a+d*5/2*c,b-d*13/3*c,a+d*5/2*c,b-d*1/3*c,a+d*7/2*c,b-d*c, outline='black', fill='white')
    for i in range(1,4):
        lodka(100,390,30,1/1)
        lodka(270,290,30,1/4)
        lodka(200,325,30,1/2)
