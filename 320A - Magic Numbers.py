s = input()
flag=1
for i in range(len(s)):
    if s[i] != "1" and s[i]!="4" :
        # print("NO")
        flag=0
    elif s[i:i+3]=="444" :
        # print("NO")
        flag=0
if s[0]=="4":
    flag=0
if (flag == 0):
    print("NO")
else:    
    print("YES")
# print(s)
