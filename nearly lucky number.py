num=input()
num=list(num)
#print(num)
count=0
for i in num:
    if i=='4' or i=='7':
        count=count+1
#print(count)
if count==4 or count==7:
    print('YES')
else:
    print('NO')
