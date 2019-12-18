import tkinter

X_MAX, Y_MAX= 800,600

canvas=tkinter.Canvas(width=X_MAX, height=Y_MAX, bg='white')
canvas.pack()

xx,yy=0,0

def klik(event):
    x=event.x
    y=event.y
    canvas.create_oval(x-5,y-5,x+5,y+5, fill='red')
    global xx,yy
    xx,yy=x,y

def pusti(event):
    x=event.x
    y=event.y
    canvas.create_oval(x-5,y-5,x+5,y+5, fill='blue')
    canvas.create_line(xx,yy,x,y)

canvas.bind('<ButtonPress>', klik)
canvas.bind('<ButtonRelease>', pusti)
