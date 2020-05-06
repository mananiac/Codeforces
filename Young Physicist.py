countx,county,countz = 0,0,0

for _ in range(int(input())):
    x,y,z = map(int,input().split())
    countx,county,countz = countx+x,county+y,countz+z
#print(x,y,z)
if(countz==0 and county==0 and countx==0)  :
    print("YES")
else:
    print("NO")
