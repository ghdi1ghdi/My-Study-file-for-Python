def total():
    global cnt
    cnt = 0
    for i in range(10):
        cnt=cnt+1
        print("내부:",cnt)
    return cnt


aa=total()
print("외부호출변수:",cnt)
#print("외부최종:",aa)
