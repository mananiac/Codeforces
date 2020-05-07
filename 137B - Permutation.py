s = int(input())
arr=list(map(int,input().split()))
count = 0
d=set()

for i in range(s):
    if (arr[i] <=s) and (arr[i] not in d):
        d.add(arr[i])
        count=count+1
print(s-count)        
