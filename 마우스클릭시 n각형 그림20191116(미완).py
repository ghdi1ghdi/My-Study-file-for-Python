input("몇각형을 사용하시겠습니까?")
import turtle
t=turtle.Turtle()
def square(length):
    for i in range(4):
        t.forward(length)
        t.left(90)
def triangle(length):
    for i in range(3):
        t.forward(length)
        t.left(120)
def drawit(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.color("red")
    square(50)
    t.end_fill()
    
s=turtle.Screen()
s.onscreenclick(drawit)
