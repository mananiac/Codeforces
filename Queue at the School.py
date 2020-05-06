m=list(map(int,input().split()))
num=m[0]
times=m[1]
names=list(input())
a=num
str=""
while(times>0):
    for i in range(0,num):
        #while(times>0):
            if(i==(num-1)):
                continue
            elif(i==a):
                continue
            elif(names[i] == 'B' and names[i+1] == 'G'):
                a=i+1
                temp=names[i+1]
                names[i+1]=names[i]
                names[i]=temp
    a=num            

    times=times-1
#print(names)
for k in names:
    str=str+k
    #print(str)
print(str)
