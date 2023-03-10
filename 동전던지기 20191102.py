import turtle
import random
t= turtle.Turtle()
screen=turtle.Screen()

image1="D:\python\image python\\front.gif"
image2="D:\python\image python\\back.gif"

screen.addshape(image1)
screen.addshape(image2)
t1=turtle.Turtle()
coin=random.randint(0,1)
if coin ==0:
    t1.shape(image1)
    t1.stamp()
else:
    t1.shape(image2)
    t1.stamp()
