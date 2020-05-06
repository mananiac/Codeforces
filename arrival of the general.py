Vaibhav = int(input())
arr =list(map(int,input().split()))
mini = arr[Vaibhav-1]
maxi = arr[0]
maxPos = 0
minPos = Vaibhav-1
swaps = 0
for i in range(0,Vaibhav):
    
 #10 10 58 31 63 40 76  
#  7
# 10 10 58 31 63 40 76
    if arr[i] > maxi:
        maxi = arr[i]
        maxPos = i
    if arr[i] <= mini:
        mini = arr[i]  
        minPos =i
swaps = swaps + Vaibhav - minPos -1   +maxPos        
if (maxPos>minPos):
    swaps = swaps-1
# print(maxPos,minPos)    
   
##################################
print(swaps)