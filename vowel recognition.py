test=int(input())

for i in range(test):
    num=input()
    a=[]
    count=1
    for i in range(0,len(num)):
        for j in range(i,len(num)):
            for k in range(j,len(num)):
                if num[i:j+1] in a:
                    continue
                else:
                    a.append(num[i:j+1])
    #print(a)
    for i in a:
        for j in range(0,len(i)) :
            if (i[j]== "a" or i[j]== "e" or i[j]=="i"or i[j]=="o" or i[j]=="u" or i[j]=="A" or i[j]=="E" or i[j]=="I" or i[j]=="O" or i[j]=="U" ):
                count=count+1

                #print(i[j],end=" ")

    print(count)


    correct-----------------
    test=int(input())

for i in range(test):
    num=input()
    a=[]
    count=0
# for i in num:
    for j in range(0,len(num)):
        if (num[j]== "a" or num[j]== "e" or num[j]=="i"or num[j]=="o" or num[j]=="u" or num[j]=="A" or num[j]=="E" or num[j]=="I" or num[j]=="O" or num[j]=="U" ):
            count=count+(len(num)-j) * (j+1)
    print(count)
   # (strlen -i) * (i+1)
