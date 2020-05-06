a=int(input())
num=list(map(int,input().split()))
count=1
max=1
for i in range(0,a):
    if i==a-1:
        continue
    elif num[i+1]>=num[i]:
        count=count+1
        if count>max:
            max=count

    else:
        count=1

print(max)
