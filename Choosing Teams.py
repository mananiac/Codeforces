n, k = map(int,input().split())
arr = list(map(int,input().split()))
total = 5
ans=0
atMost = total - k
count = 0
for i in range(0,n):
    if arr[i]<=atMost:
        count+=1
ans=count//3
print(ans)