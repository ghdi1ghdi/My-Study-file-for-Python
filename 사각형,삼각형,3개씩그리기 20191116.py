import turtle
t=turtle.Turtle()
def square(length):#length는 한변의 길이
    for i in range(4):
        t.forward(length)
        t.left(90)
t.up()
t.goto(-200,0)
t.down()
square(100)
t.up()
t.goto(0,0)
t.down()
square(100)
t.up()
t.goto(200,0)
t.down()
square(100);


def triangle(length):
    for i in range(3):
        t.forward(length)
        t.left(120)
t.up()
t.goto(-200,-150)
t.down()
triangle(100)
t.up()
t.goto(0,-150)
t.down()
triangle(100)
t.up()
t.goto(200,-150)
t.down()
triangle(100);
