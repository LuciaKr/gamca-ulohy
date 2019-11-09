import tkinter
import random
canvas=tkinter.Canvas(width=800, height=600, bg='white')
canvas.pack()

def vlak(x,y,f,k,w,p):
    for i in range(1,p):
        canvas.create_line(x,y,x+150,y,width=w)
        canvas.create_rectangle(x+10,y-70,x+140,y+10,fill=f)
        canvas.create_oval(x+25,y-5,x+55,y+25,fill=k)
        canvas.create_oval(x+95,y-5,x+125,y+25,fill=k)
        x+=150

vlak(50,100, 'red','black',3,5)
vlak(50,200, 'green','black',3,3)
vlak(50,300,'blue','black',3,4)
