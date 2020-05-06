num = int(input())
arr = list(map(int,input().split()))
maxPockets=1

for i in range(num):
    count=0
    for j in range(i,num):
        # if j>=num:
        #     if arr[i] == arr[j]:
        #         count+=1
        # continue    
        if arr[i] == arr[j]:
            count+=1
    if count>=maxPockets:
        maxPockets= count
print(maxPockets)    