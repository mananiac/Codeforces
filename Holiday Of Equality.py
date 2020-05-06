no = int(input())
num=[]
#for i in range(no):
num=list(map(int,input().split()))
    #num.append(int(input()))

largest=num[0]
for i in range(0,len(num)):
    if(num[i]>largest ):
        largest=num[i]


count=0
for i in range(no):
    count=count+(largest-num[i])
    #print(count)
if(no==1):
    print("0")
else:
    print(count)
#print(largest) 
