cursor=0
key=list()
key=input()
if "S" in key:
    s=key.count("S")
    print(s)
    cursor=cursor+1*s
    if "T" in key:
        t=key.count("T")
        print(t)
while((4*t)/cursor!=1):
    cursor=cursor+1
    print(cursor)
print(cursor)
