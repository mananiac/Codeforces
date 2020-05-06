num1=input()
num2=input()
num3=""
for i in range(len(num1)-1,-1,-1):
    num3=num3+num1[i]
if(num2==num3):
    print('YES')
else:
    print('NO')
