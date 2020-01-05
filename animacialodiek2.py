import tkinter
import random
canvas=tkinter.Canvas(width=800, height=600, bg='white')
canvas.pack()

y=random.randint(60,200)
#canvas.create_rectangle(0,300,800,600, outline='dark blue', fill='dark blue')

def mesiac(x,color,outline):
    canvas.create_oval(x,y,x+50,y+50, fill=color, outline=outline)

def odraz(x,color,outline):
    canvas.create_oval(x,600-y,x+50,550-y, fill=color, outline=outline)

def vlajka(x,y,color):
    canvas.create_oval(x,y,x+100,y+100, outline='black',fill='brown')
    canvas.create_rectangle(x,300,x+100,400,outline='dark blue', fill='dark blue')
    canvas.create_line(x+50,100,x+50,270)
    canvas.create_rectangle(x+50,100,x+170,y-85, fill=color)

def mesiacik(x,y,r,color,fill):
    canvas.create_oval(x,y,x+r,y+r,outline=color, fill=fill)

def lodka(x,y,a):
    canvas.create_rectangle(x+70*a,y-130*a,x+80*a,y+a, outline='brown', fill='brown')
    canvas.create_polygon(x,y,x+30*a,y+60*a,x+120*a,y+60*a,x+150*a,y, outline='black', fill='saddle brown')
    canvas.create_polygon(x+75*a,y-130*a,x+75*a,y-10*a,x+105*a,y-30*a, outline='black', fill='white')

    canvas.create_oval(x+75*a,y+20*a,x+95*a,y+40*a,fill='light blue', outline='light blue')
    canvas.create_oval(x+55*a,y+20*a,x+75*a,y+40*a,fill='light blue', outline='light blue')
    canvas.create_oval(x+85*a,y+20*a,x+105*a,y+40*a,fill='saddle brown', outline='saddle brown')
    canvas.create_oval(x+45*a,y+20*a,x+65*a,y+40*a,fill='saddle brown', outline='saddle brown')

def pozadie():
    canvas.create_rectangle(0,300,800,600, outline='dark blue', fill='dark blue')

    mesiac(450, 'yellow', 'yellow')
    mesiac(465,'white', 'white')

    odraz(450, 'yellow', 'yellow')
    odraz(465, 'dark blue', 'dark blue')

    vlajka(30,270, 'green')
    vlajka(600,270, 'red')

    mesiacik(120,122,40,'red', 'red')
    mesiacik(135,122,40, 'green', 'green')
    mesiacik(680, 100+55/2, 30, 'light blue', 'light blue')
    mesiacik(670,100+55/2, 30, 'red', 'red')
    mesiacik(710,100+55/2,30,'light blue', 'light blue' )
    mesiacik(720,100+55/2,30,'red', 'red' )

for i in range(0,800-100+10+1,10):
    canvas.delete("all")
    pozadie()

    lodka(270+i,290,1/4)
    lodka(200+2*i,325,1/2)
    lodka(100+4*i,390,1)
    
    canvas.update()
    canvas.after(100)
