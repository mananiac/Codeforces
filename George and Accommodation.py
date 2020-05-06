num=int(input())
count=0
for i in range(0,num):
    a,b=map(int,input().split())
    #print(a,b)
    if(b-a>2 or b-a==2):
        count=count+1
        #print(count)
print(count)
