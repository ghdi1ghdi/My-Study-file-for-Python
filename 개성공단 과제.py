def birthday():
    year= input()
    month=input()
    day=input()
    print(year+"."+month+"."+day)

def num():
    m=int(input())
    n=int(input())
    print(m+n)
def str():
    m= input()
    n= input()
    print(m+n)
def ty():
    m=input()
    n=float(m)
    print(n)
def showtype():
    m=input()
    print(m,type(m))
def removesame():
    a={1,1,1,2,2,3,3,3,4,4,5}
    a_set=set(a)
    a_list = list(a_set)
    print(a_list)
