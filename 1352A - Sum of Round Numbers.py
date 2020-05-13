for _ in range(int(input())):
    num = int(input())
    a=[]
    i=1
    count=0
    b=""
    while(num>0):
        r=num%10
        a.append(r*i)
        i=i*10
        num=num//10
    # a.sort(reverse=True)
    for i in range(len(a)):
        if a[i] != 0:
            count=count+1
            b= b+ str(a[i]) + " "
    print(count)        
    print(b)
        