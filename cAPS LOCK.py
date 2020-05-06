num=input()
num2=num
num2=list(num)
j=num2.pop(0)
num3=""

for i in num2:
    num3=num3+i
#print(num2)
if num.isupper() :
    print(num.lower())
elif(len(num)==1)    :
    if num.isupper():
        print(num)
    else:
        print(num.upper())
elif(num3.isupper() and j.islower() ):
    print(num.title())
else:
    print(num)
