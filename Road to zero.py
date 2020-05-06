for i in range(int(input() )):
    x , y  = map(int,input().split())
    a , b  = map(int,input().split())

    total=0
    cost = 0
    num=0
    blabla = a*(x+y)
    if(x == y):
        total =y
        num=0
    elif(x<y):
        num=y-x
        total=x
    elif(y<x):
        num=x-y
        total=y
    cost = (num*a) + (total*b)
    print(min(cost,blabla))
