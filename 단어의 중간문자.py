a=input("단어를 입력하세요.")
b=len(a)
print(b)
print(b%2)
if b%2==0:
    print(a[int(b/2)])
    print(a[int(b/2-1)])
if b%2!=0:
    print(a[int(b/2)])

    
