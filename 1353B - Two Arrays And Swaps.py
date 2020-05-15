for i in range(int ( input() ) ):
    n,k = map(int,input().split())
    arr1= list(map(int,input().split()))
    arr2= list(map(int,input().split()))
    arr1.sort()
    arr2.sort(reverse=True)
    for i in range(k):
        temp =0
        if arr1[i]>=arr2[i]: 
            break
        if arr1[i]<arr2[i]:
            temp = arr1[i]
            arr1[i]= arr2[i]
            arr2[i] = temp
        
    print(sum(arr1))
    # print(arr1,arr2)
   