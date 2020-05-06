num=list(input())
arr=[]
arr=list(arr)
str=""
for i in range(0,len(num)):
    if(num[i]=='h'):
        arr.append(num[i])
        for j in range(i+1,len(num)):
            if(num[j]=='e'):
                arr.append(num[j])
                for k in range(j+1,len(num)):
                    if(num[k]=='l'):
                        arr.append(num[k])
                        for l in range(k+1,len(num)):
                            if(num[l]=='l'):
                                arr.append(num[l])
                                for m in range(l+1,len(num)):
                                    if(num[m]=='o'):
                                        arr.append(num[m])

                                    else:
                                        continue

                            else:
                                continue

                    else:
                        continue

            else:
                continue

    else:
        continue
#print(arr)
if (len(arr) < 5):
    print("NO")
elif(arr[0]=='h' and arr[1]=='e' and arr[2]=='l' and arr[3]=='l' and arr[4]=='o' ):
    print("YES")
else:
    print("NO")
 
