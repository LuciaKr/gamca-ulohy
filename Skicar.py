import tkinter
from random import randrange, randint

X_MAX, Y_MAX = 800, 600

canvas=tkinter.Canvas(width=X_MAX,height=Y_MAX,bg='white')
canvas.pack()

xx,yy=0,0
hrubka=5
farba='black'

def tlacitka():
    canvas.create_rectangle(3,550,53,600)
    canvas.create_rectangle(53,550,103,600)
    canvas.create_rectangle(103,550,153,600)

    canvas.create_oval(23,570,33,580, fill='black')
    canvas.create_oval(68,565,88,585, fill='black')
    canvas.create_oval(113,560,143,590, fill='black')

    canvas.create_rectangle(176,550,376,600)
    canvas.create_text(276,575,text='delete', font='typewriter 20')

    canvas.create_rectangle(750,550,800,600, fill='black')
    canvas.create_rectangle(700,550,750,600, fill='pink')
    canvas.create_rectangle(650,550,700,600, fill='purple')
    canvas.create_rectangle(600,550,650,600, fill='sky blue')
    canvas.create_rectangle(550,550,600,600, fill='green')
    canvas.create_rectangle(500,550,550,600, fill='yellow')
    canvas.create_rectangle(450,550,500,600, fill='orange')
    canvas.create_rectangle(400,550,450,600, fill='red')

def vyber_tlacitka(event):
    global xx,yy
    global hrubka
    global farba
    canvas.bind('<B1-Motion>',ciarka)
    xx,yy=event.x,event.y
    x,y=event.x,event.y

    if  y >= 550 and 53 > x >= 3:
        hrubka=2
    elif y >= 550 and 103 > x >= 53:
        hrubka=4
    elif y >= 550 and 153 > x >= 103:
        hrubka=7
    else:
        pass

    if 376 > x >= 176 and 550 < y <= 600:
        canvas.delete('all')
        tlacitka()

    if y >= 550 and 450 > x >= 400:
        farba='red'
    elif y >= 550 and 500 > x >= 450:
        farba='orange'
    elif y >= 550 and 550 > x >= 500:
        farba='yellow'
    elif y >= 550 and 600 > x >= 550:
        farba='green'
    elif y >= 550 and 650 >x >= 600:
        farba='sky blue'
    elif y >= 550 and 700 > x >= 650:
        farba='purple'
    elif y >= 550 and 750 > x >= 700:
        farba='pink'
    elif y >= 550 and 800 > x >= 750:
        farba='black'
    else:
        pass

def ciarka(event):
    global xx,yy
    x,y=event.x,event.y
    canvas.create_line(xx,yy,x,y, width=hrubka, fill=farba)
    xx,yy=x,y

tlacitka()   
canvas.bind('<Button-1>', vyber_tlacitka)
