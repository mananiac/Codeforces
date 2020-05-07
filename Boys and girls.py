# import pdb
b, g = map(int,input().split())
# pdb.set_trace()
arr = [b+g]
string =""
total = b+g
if (g>=b):
    arr = ["G"]*(b+g)
    for i in range(0,2*b,2):
        arr[i]="B"
        
elif (b>g):
    arr = ["B"]*(b+g)
    for i in range(0,2*g,2):
        arr[i]="G"
        
for i in arr:
    string = string + i
print(string)    