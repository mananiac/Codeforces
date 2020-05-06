from collections import Counter 
x = list(input())
y = list(input())
z = list(input())

counterxy = Counter(x) + Counter(y)
counterz = Counter(z)
print(counterxy)
print(counterz)
if counterxy == counterz:
    print("YES")
else:
    print("NO")