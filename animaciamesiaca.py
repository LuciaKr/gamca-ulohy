import tkinter
import random
canvas=tkinter.Canvas(width=800, height=600, bg='white')
canvas.pack()

y=random.randint(60,150)

#canvas.create_rectangle(0,300,800,600, outline='dark blue',fill='dark blue')

def mesiac(a,b,r,color,fill):
    canvas.create_oval(a,b,a+r,b+r,outline=color,fill=fill)
        
#mesiac(465,275-y,50,'white','yellow')
#mesiac(480,275-y,50,'white','white')
#mesiac(465,275+y,50,'dark blue','yellow')
#mesiac(480,275+y,50,'dark blue','dark blue')
    
def vlajka(a,b,color):
    canvas.create_oval(a,b,a+100,b+100, outline='black',fill='brown')
    canvas.create_rectangle(a,300,a+100,400,outline='dark blue',fill='dark blue')
    canvas.create_line(a+50,100,a+50,270)
    canvas.create_rectangle(a+50,100,a+170,b-85,fill=color)

#vlajka(30,270,'green')
#vlajka(600,270,'red')

#mesiac(120,122,40,'red','red')
#mesiac(135,122,40,'green','green')

#mesiac(680,100+55/2,30,'light blue','light blue')
#mesiac(670,100+55/2,30,'red','red')
#mesiac(710,100+55/2,30,'light blue','light blue' )
#mesiac(720,100+55/2,30,'red','red')

#mesiac(465,275-y,50,'white','yellow')
#mesiac(480,275-y,50,'white','white')
#mesiac(465,275+y,50,'dark blue','yellow')
#mesiac(480,275+y,50,'dark blue','dark blue')

def lodka(a,b,z):
    canvas.create_rectangle(a+z*70,b-z*130,a+z*80,b+z,outline='brown',fill='brown')
    canvas.create_polygon(a+z,b+z,a+z*30,b+z*60,a+z*120,b+z*60,a+z*150,b+z,outline='black',fill='saddle brown')
    canvas.create_polygon(a+z*75,b-z*130,a+z*75,b-z*10,a+z*105,b-z*30,outline='black',fill='white')

    canvas.create_oval(a+z*55,b+z*20,a+z*75,b+z*40,fill='light blue',outline='light blue')
    canvas.create_oval(a+z*50,b+z*20,a+z*70,b+z*40,fill='saddle brown',outline='saddle brown')
    canvas.create_oval(a+z*75,b+z*20,a+z*95,b+z*40,fill='light blue',outline='light blue')
    canvas.create_oval(a+z*80,b+z*20,a+z*100,b+z*40,fill='saddle brown',outline='saddle brown')

#a=[150,250,320]
#b=[390,325,290]
#z=1

#for i in range(1,4):
    #lodka(a[i-1],b[i-1],z)
    #z/=2

for i in range(7):
    canvas.delete('all')

    canvas.create_rectangle(0,300,800,600, outline='dark blue',fill='dark blue')

    mesiac(465,275-y,50,'white','yellow')
    mesiac(480,275-y,50,'white','white')
    mesiac(465,275+y,50,'dark blue','yellow')
    mesiac(480,275+y,50,'dark blue','dark blue')

    vlajka(30,270,'green')
    vlajka(600,270,'red')

    mesiac(120,122,40,'red','red')
    mesiac(135,122,40,'green','green')

    mesiac(680,100+55/2,30,'light blue','light blue')
    mesiac(670,100+55/2,30,'red','red')
    mesiac(710,100+55/2,30,'light blue','light blue' )
    mesiac(720,100+55/2,30,'red','red')

    mesiac(465,275-y,50,'white','yellow')
    mesiac(480,275-y,50,'white','white')
    mesiac(465,275+y,50,'dark blue','yellow')
    mesiac(480,275+y,50,'dark blue','dark blue')

    a=[150,250,320]
    b=[390,325,290]
    z=1

    for i in range(1,4):
        lodka(a[i-1],b[i-1],z)
        z/=2

    y=y+10    
    
    canvas.update()
    canvas.after(100)
