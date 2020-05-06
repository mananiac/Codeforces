
p=int(input())
num=list(map(int,input().split()))
num1=[]
count=0
flag=0
max=0
a=p
num1.append(num[0])
while(flag==1):
    for i in range(1,p-1):
        # if i=p-2:
        #     num1.append(num[len(num)])
        if(num[i-1] <=num[i] <=num[i+1]):
            flag=1
            continue
        # elif(a==i):
        #     continue
        else:
            if (  num[i-1]<=num[i]  <=num[i+1]  ):
                max=num[i]
                num1.append(max)
            elif(  num[i-1]<=num[i+1] <=num[i]  ):
                max=num[i+1]
                num1.append(max)
            elif(  num[i]<=num[i-1] <=num[i+1]  ):
                max=num[i-1]
                num1.append(max)
            elif(  num[i]<=num[i+1] <=num[i-1]  ):
                max=num[i+1]
                num1.append(max)
            elif(  num[i+1]<=num[i-1] <=num[i] ):
                max=num[i-1]
                num1.append(max)
            elif(  num[i+1]<=num[i] <=num[i-1]  ):
                max=num[i]
                num1.append(max)
            #a=i+1
            #num[i]=max
            flag=0
            print(num1)
    #a=p
    num1.append(num[p-1])
    num=num1
    count=count+1
# num[i-1],num[i],num[i+1]
            # if (  num[i-1]<=num[i]  <=num[i+1]  ):
            #     continue
            # elif(  num[i-1]<=num[i+1] <=num[i]  ):
            #     num[i+1],num[i]=num[i],num[i+1]
            # elif(  num[i]<=num[i-1] <=num[i+1]  ):
            #     num[i],num[i-1]=num[i-1],num[i]
            # elif(  num[i]<=num[i+1] <=num[i-1]  ):
            #     num[i-1],num[i],num[i+1]=num[i],num[i+1] ,num[i-1]
            # elif(  num[i+1]<=num[i-1] <=num[i] ):
            #     num[i-1],num[i],num[i+1]=num[i+1],num[i-1] ,num[i]
            # elif(  num[i+1]<=num[i] <=num[i-1]  ):
            #     num[i-1],num[i],num[i+1]=num[i+1],num[i] ,num[i-1]
print(count)
print(num)
print(num1)  
