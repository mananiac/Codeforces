a,b=map(int,input().split())
count=0
flag=0
if a>b:
    print(count)
else:
    while(flag==0):
        a=a*3
        b=b*2
        count=count+1
        if a>b:
            flag=1

print(count)        
