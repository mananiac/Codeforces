num =int(input())
arr=[num]
count =0

arr = list(map(int,input().split()))
for i in arr:

    count = count + i/100
count = count/num

print(count*100)    
