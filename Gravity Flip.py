a=int(input())
b=list(input().split())
for i in range (0,len(b)):
    for j in range (i,len(b)):
        if(int(b[i])>int(b[j])):
            temp = b[i]
            b[i] = b[j]
            b[j] = temp
string =""
for i in range(0,len(b)):
    string = string + " " + b[i]
print(string)
