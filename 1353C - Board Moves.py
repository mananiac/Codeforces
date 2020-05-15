for i in range(int ( input() ) ):
    # n,k = map(int,input().split())
    n = int(input())
    sum,count,flag=0,1,1
    if n==1:
        print(0)
        flag=0
    for i in range(3,n+1,2):
        sum = sum + (i*count*4)-(4*count)
        count=count+1
    if flag==1:
        
        print(sum)
    