import math
num=int(input())
m=list(map(int,input().split()))
m.sort()
#print(m)
count=0
i=0
t=0
#for i in range (0,len(m)):
if(    (m[i]==1) and (m[len(m)-1]==1)     ):
        if(       (len(m))%4==0):
            count=int(count+(len(m)-1)/4)

        elif((len(m))%4!=0):
            count=int(math.floor((count+(len(m)-1)/4)))
            # if(len(m)== 1 or len(m)== 2 or len(m)== 3):
           # count=count+1
while(len(m)!=0):
    if(m[len(m)-1]==4):
        m.pop(len(m)-1)
        count=count+1
        #print(m)
        continue
    elif(len(m)==1):
        m.pop(len(m)-1)
        #m.pop(i)

        count=count+1
    elif((m[i]+m[len(m)-1])==4):
        #print(m)
        m.pop(len(m)-1)
        m.pop(i)

        count=count+1
        #print(m)
        continue

        # for l in range (0,len(m)-1):
        #     t=t+1
        #     m.pop(len(m)-1)
        #     if(t==4):
        #         count=count+1
        #         t==0
         #break
    elif(m[len(m)-1]+m[i]<4):
        m.pop(i)
        m.pop(len(m)-1)
        count=count+1
        #print(m)
        break
    elif(m[len(m)-1]+m[i]>4):
        m.pop(i)
        m.pop(len(m)-1)
        count=count+2
        break
    else:
        m.pop(len(m)-1)
        count=count+1
        break
#print(m)
print(count)
