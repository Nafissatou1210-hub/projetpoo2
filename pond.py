from math import tan,cos,sin
from turtle import *
speed(10) 
width(5)


def triangle(n):
    for i in range(3):
        forward(n)
        left(120)
        forward(n)
    
def debut():
    forward(30)
    left(117)
    forward(35)
    right(180)
    forward(35)
    left(63)

def fin():
    left(90)
    forward(74)
    right(150)
    forward(85)
    right(119)
    forward(45)
    right(180)
    forward(45)
    left(50)
    forward(35)
    right(180)
    forward(35)
    left(123)
    forward(35)

def lesTriangle(m):
    n=40
    m = n+24
    t = 83
    for i in range(3):
        forward(n)
        triangle(n)
        left(90)
        forward(m)
        left(180)
        forward(m)
        left(90)
        forward(n)
        left(90)
        forward(t)
        left(180)
        forward(t)
        left(90)
        n = n+15
        m = n+40
        t = t+14
        if t > 97:
            n = n - 18.5
            t = t-35
            m = m-20
def ellipse(x1,y1,a,b):
        pencolor("blue")
        width(5)
        t=0
        
        while t<3.14:
            xM=x1+a*cos(t)
            yM=y1+b*sin(t)
            goto(xM,yM-2)
            t=t+0.1
        forward(400)
        setheading(0)
def deux(m):
    debut()
    lesTriangle(m)
    fin()

def lesEllipse():
    x = -400
    y = 0
    for i in range(3):
        ellipse(x,y,200,100)
        x = x+400
        y = y+1


lesEllipse()
left(180)
penup()
forward(1200)
left(180)
pendown()
for i in range(3):
    m=10
    deux(m)
    setheading(0)
    m = m+1

right(180)

penup()
forward(365)
pendown()

def lesRectangle():
    begin_fill()
    color("blue")
    def rectangle(l,L):
        
        begin_fill()
        color("blue")
        for i in range(2):
            forward(l)
            left(90)
            forward(L)
            left(90)
        end_fill()
    rectangle(70,20)
    begin_fill()
    color("blue")
    up()
    forward(70)
    left(90)
    forward(20)
    down()
    right(90)
    forward(20)
    left(90)
    forward(20)
    left(90)
    forward(20+70+20)
    left(90)
    forward(20)
    left(90)
    forward(20)

    end_fill()
lesRectangle()
up()
forward(400)
right(90)
forward(23)
left(90)
down()

lesRectangle()


done()