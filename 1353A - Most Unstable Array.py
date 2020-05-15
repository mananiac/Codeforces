for _ in range(int(input())):
    n,b=map(int,input().split())
    if(n==2):
        print(b)
    elif(n==1):
        print(0)
    else:
        print(2*b)
    