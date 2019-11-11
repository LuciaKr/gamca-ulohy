import tkinter
import random
canvas=tkinter.Canvas(width=800, height=600, bg='white')
canvas.pack()

def dazd(x,y):
    canvas.create_oval(x-5,y-5,x+5,y+5,fill='Powderblue')

for i in range(100):
    canvas.delete('all')

    for i in range(100):
        dazd(random.randint(10,790),random.randint(10,590))
        x=random.randint(10,790)
        y=random.randint(10,590)
    
    canvas.update()
    canvas.after(100)


