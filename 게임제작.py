import os

import turtle

import time

from time import sleep

import random



delay = 0.1

score = 0

high_score = 0

segments = []



wn = turtle.Screen()

wn.title("Snake Game")

wn.bgcolor("lime")

wn.setup(width=600, height=600)

wn.tracer(0)   # 화면 갱신 중지



# 뱀 머리

head = turtle.Turtle()

head.speed(0)

head.shape("square")

head.color("blue")

head.penup()

head.goto(0,0)

head.direction = "stop"



# 음식

food = turtle.Turtle()

food.speed(0)

food.shape("circle")

food.color("red")

food.penup()

food.goto(0,100)

#폭탄1

invincibility=turtle.Turtle()

invincibility.speed(0)

invincibility.shape("triangle")

invincibility.color("purple")

invincibility.penup()

invincibility.goto(0,-100)

#폭탄2

invincibility1=turtle.Turtle()

invincibility1.speed(0)

invincibility1.shape("triangle")

invincibility1.color("purple")

invincibility1.penup()

invincibility1.goto(0,50)

#폭탄3
invincibility2=turtle.Turtle()

invincibility2.speed(0)

invincibility2.shape("triangle")

invincibility2.color("purple")

invincibility2.penup()

invincibility2.goto(0,-50)



# 펜

pen = turtle.Turtle()

pen.speed(0)

pen.shape("square")

pen.color("black")

pen.penup()

pen.hideturtle()

pen.goto(0, 260)

pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal")) 



# 사용자 함수 정의 



def go_up():

    if head.direction != "down":

        head.direction = "up"



def go_down():

    if head.direction != "up":    

        head.direction = "down"



def go_left():

    if head.direction != "right":    

        head.direction = "left"



def go_right():

    if head.direction != "left":    

        head.direction = "right"    



def move():

    if head.direction == "up":

        y = head.ycor()

        head.sety(y + 20)

    if head.direction == "down":

        y = head.ycor()

        head.sety(y - 20)

    if head.direction == "left":

        x = head.xcor()

        head.setx(x - 20)

    if head.direction == "right":

        x = head.xcor()

        head.setx(x + 20)



# 벽이나 자신에게 접촉한 경우 초기화 처리 

def reset():
    global score, delay

    segments.clear()

    score = 0

    delay = 0.1            

    pen.clear()    

    pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))        



# 키보드 값을 처리할 메소드 연결

wn.listen()

wn.onkeypress(go_up, "w")

wn.onkeypress(go_down, "s")

wn.onkeypress(go_left, "a")

wn.onkeypress(go_right, "d")



# 게임 처리 부분

while True:

    wn.update() # 화면 갱신 



    # 벽 충돌 검사 처리

    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290 or head.distance(invincibility)<20 or head.distance(invincibility1)<20 or head.distance(invincibility2)<20:

        time.sleep(1)

        head.goto(0,0)

        head.direction = "stop"        

    # 뱀 몸통 숨김

        for segment in segments:

            segment.goto(1000, 1000)

    # 뱀과 점수  초기화 

        reset()

        

    # 음식을 먹었는지 검사 처리 

    if head.distance(food) < 20:

        # 음식을 임의 위치에 새로 놓음(옮김)

        x = random.randint(-270, 270)

        y = random.randint(-270, 270)

        food.goto(x, y)
        

        # 뱀 몸통 추가

        new_segment = turtle.Turtle()

        new_segment.speed(0)

        new_segment.shape("square")

        new_segment.color("skyblue")

        new_segment.penup()

        segments.append(new_segment)

        # 지연 시간 줄임

        delay -= 0.001

        # 점수 올리고, 최고 점수보다 높으면 갱신 처리

        score += 10

        if score > high_score:

            high_score = score

        pen.clear() # 점수 문자열 부분 지움   

        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))    



    # 몸통 위치 이동 

    for index in range(len(segments)-1, 0, -1):

        x = segments[index-1].xcor()

        y = segments[index-1].ycor()

        segments[index].goto(x,y)
  

    # 0번 몸통을 머리 위치로 이동

    if len(segments) > 0:

        x = head.xcor()

        y = head.ycor()

        segments[0].goto(x,y)

        

    # 머리 이동 처리      

    move()

    #폭탄 임의 위치 이동

    if head.distance(food)<20:
     
        x = random.randint(-270,270)
        
        y = random.randint(-270,270)

        invincibility.goto(x,y)
        
    #폭탄 임의 위치 이동

    if head.distance(food)<20:
     
        x = random.randint(-270,270)
        
        y = random.randint(-270,270)

        invincibility1.goto(x,y)

     
    #폭탄 임의 위치 이동

    if head.distance(food)<20:
     
        x = random.randint(-270,270)
        
        y = random.randint(-270,270)

        invincibility2.goto(x,y)
            
        # 머리가 몸통과 접촉했는지 검사 처리 

    for segment in segments:

        if segment.distance(head) < 20:

            time.sleep(1)

            head.goto(0,0)

            head.direction = "stop"

            # Hide the segments

            for segment in segments:

                segment.goto(1000, 1000)

            # Reset

            reset()         

    

    time.sleep(delay)  # 시간 지연 



wn.mainloop()
