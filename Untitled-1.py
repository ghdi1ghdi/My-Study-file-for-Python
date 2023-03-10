import random

how_many = 3
won = 0
dic={"가위":1, "보":2, "가위":3}

for i in range(how_many):
    ai = random.randint(1,3)
    while True:
        pl= input("가위:1 바위:2 보:3입니다. 가위바위보를 입력하세요.")
        if pl in dic.keys():
            break

    sub = dic[pl]-ai
    if sub ==0:
        print("무승부")
    elif sub == 1 or sub ==-2:
        print("승리")
        won +=1
    else:
        print("패배")
print(f"you won {won} out of {how_many}")