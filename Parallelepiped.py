# countx,county,countz = 0,0,0

# for _ in range(int(input())):
x,y,z = map(int,input().split())
x,y,z = (x*y)/z,(y*z)/x,(x*z)/y
x,y,z = int(x**0.5),int(y**0.5),int(z**0.5)

sum = (x+y+z)*4
print(sum)
