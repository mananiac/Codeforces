for _ in range(int(input())):
    a,b = map(int,input().split())
    arr=[]
    flag=0
    c=""
    lastodd = (a-(b-1))
    lasteven = (a-2*(b-1))
    if (lastodd > 0 and lastodd % 2 == 1): 
        flag=1
        arr = [1 for _ in range(b)]
        arr[len(arr)-1] = lastodd
    if (lasteven > 0 and lasteven % 2 == 0):  
        flag=1
        arr = [2 for _ in range(b)]
        arr[len(arr)-1] = lasteven
    if flag ==0:
        print("NO")
    if flag == 1:
        print("YES")
        for i in arr:
            c=c+str(i)+" "
        print(c)
    