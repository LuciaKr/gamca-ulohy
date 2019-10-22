import tkinter
import random
canvas=tkinter.Canvas(width=800, height=600, bg='white')
canvas.pack()

y=random.randint(60,200)
canvas.create_rectangle(0,300,800,600, outline='dark blue', fill='dark blue')

def mesiac(x, color, outline):
    canvas.create_oval(x,y,x+50,y+50, fill=color, outline=outline)
mesiac(450, 'yellow', 'yellow')
mesiac(465,'white', 'white')

def odraz(x, color, outline):
    canvas.create_oval(x,600-y,x+50,550-y, fill=color, outline=outline)
odraz(450, 'yellow', 'yellow')
odraz(465, 'dark blue', 'dark blue')

def vlajka(a,b,c,color):
    canvas.create_oval(a,b,a+100,b+100, outline='black',fill='brown')
    canvas.create_rectangle(a,300,a+100,400,outline='dark blue', fill='dark blue')
    canvas.create_line(a+50,100,a+50,270)
    canvas.create_rectangle(a+50,c,a+170,b-85, fill=color)
vlajka(30,270,100, 'green')
vlajka(600,270,100, 'red')

def mesiacik(d,e,r, color, fill):
    canvas.create_oval(d,e,d+r,e+r,outline=color, fill=fill)
    
mesiacik(120,122,40,'red', 'red')
mesiacik(135,122,40, 'green', 'green')
mesiacik(680, 100+55/2, 30, 'light blue', 'light blue')
mesiacik(670,100+55/2, 30, 'red', 'red')
mesiacik(710,100+55/2,30,'light blue', 'light blue' )
mesiacik(720,100+55/2,30,'red', 'red' )


def lodka(a,b, c, d):
    canvas.create_rectangle(a+d*7/3*c,b-d*13/3*c,a+d*8/3*c,b+d, outline='brown', fill='brown')
    canvas.create_polygon(a+d,b+d,a+d*c,b+d*2*c,a+d*4*c,b+d*2*c,a+d*5*c,b+d, outline='black', fill='saddle brown')
    canvas.create_polygon(a+d*5/2*c,b-d*13/3*c,a+d*5/2*c,b-d*1/3*c,a+d*7/2*c,b-d*c, outline='black', fill='white')       
lodka(270,290,30,1/4)
lodka(200,325,30,1/2)
lodka(100,390,30,1/1)   

def dvojity_mesiacik(a,b,r,color,outline):
    canvas.create_oval(a,b,a+r,b+r,fill=color, outline=outline )
dvojity_mesiacik(155,391+39/2,20, 'light blue', 'light blue')
dvojity_mesiacik(175,391+39/2,20, 'light blue', 'light blue')
dvojity_mesiacik(150,391+39/2,20, 'saddle brown', 'saddle brown')
dvojity_mesiacik(180,391+39/2,20, 'saddle brown', 'saddle brown')

dvojity_mesiacik(899/4,651/2+39/4,10, 'light blue', 'light blue')
dvojity_mesiacik(949/4,651/2+39/4,10, 'light blue', 'light blue')
dvojity_mesiacik(889/4,651/2+39/4,10, 'saddle brown', 'saddle brown')
dvojity_mesiacik(959/4,651/2+39/4,10, 'saddle brown', 'saddle brown')


dvojity_mesiacik(1135/4,2359/8,5, 'light blue', 'light blue')
dvojity_mesiacik(1155/4,2359/8,5, 'light blue', 'light blue')
dvojity_mesiacik(1125/4,2359/8,5, 'saddle brown', 'saddle brown')
dvojity_mesiacik(1165/4,2359/8,5, 'saddle brown', 'saddle brown')










