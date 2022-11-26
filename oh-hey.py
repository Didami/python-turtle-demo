from turtle import *

def iWanna():
    color('red')
    begin_poly()
    pensize(10)
    left(50)
    forward(133)
    circle(50, 200)
    right(140)
    circle(50, 200)
    forward(133)
    end_poly()

def be():
    penup()
    setheading(90)
    setpos(0, 60)
    pendown()

def yours():
    color('white')
    right(30)
    forward(60)
    penup()
    setpos(0, 60)
    pendown()
    setheading(90)
    left(30)
    forward(60)

Screen().bgcolor('black')
iWanna()
be()
yours()
exitonclick()
