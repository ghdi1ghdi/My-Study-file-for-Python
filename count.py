infile=open("서시.txt", "r", encoding="utf-8")

count=0
for line in infile:
    count+=1
    print(count,line,end="")
    if (count==14):
        count+=1
        print(count,line,end="")

infile.close()