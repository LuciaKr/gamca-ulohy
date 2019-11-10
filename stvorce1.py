import tkinter
import random

X_MAX,Y_MAX = 800,600

canvas=tkinter.Canvas(width=X_MAX, height=Y_MAX)
canvas.pack()

def stvorce(r,x,y,p,m):
    for i in range(p):
        canvas.create_rectangle(x-r/2,y-r/2,x+r/2,y+r/2)
        r-=m

#for i in range(1,101):
    #stvorce(random.randint(150,300),random.randint(r,X_MAX-r),random.randint(r,Y_MAX-r),random.randint(5,10))

r=random.randint(150,300)
m=random.randint(10,20)

p=random.randint(5,10)

for i in range(1,11):
    stvorce(random.randint(150,300),random.randint(r,X_MAX-r),random.randint(r,Y_MAX-r),p,m)
    p=random.randint(5,10)

