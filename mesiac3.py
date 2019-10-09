import tkinter
import random
canvas=tkinter.Canvas(width=800, height=600, bg='white')
canvas.pack()

def mesiac(x,y,pozadie='white'):
    canvas.create_rectangle(0,300,800,600, fill='dark blue')
    canvas.create_oval(x,300-y,x+50,250-y, outline='yellow', fill='yellow')
    canvas.create_oval(x+15,300-y,x+65,250-y, outline='white', fill='white')
    canvas.create_oval(x,300+y,x+50,350+y, outline='yellow', fill='yellow')
    canvas.create_oval(x+15,300+y,x+65,350+y, outline='dark blue', fill='dark blue')
mesiac(450,random.randint(10,200),"white")

    
def vlajka(a,b,farba='green'):
    for i in range(1,3):
        canvas.create_oval(a,b,a+100,b+100, outline='black',fill='brown')
        canvas.create_rectangle(a,30+b,a+100,b+130,outline='dark blue', fill='dark blue')
        a=a*20
    canvas.create_line(80,100,80,270)
    canvas.create_rectangle(80,100,200,185, fill='green')
        
vlajka(30,270)





