num =int(input())
arr = [[0]*2 for _ in range(num)]
h=[]
a=[]
count =0
for i in range(num):
    arr[i] =list(map(int,input().split()))
for i in range(num):
    for j in range(1,num):
        if (i+j>=(num)):
            break

        
        if(arr[i][0] == arr[j+i][1]):
            count +=1
        if(arr[i][1] == arr[j+i][0]):  
            count +=1
          
print(count)    