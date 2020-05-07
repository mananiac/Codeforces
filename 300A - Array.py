num = int(input())
arr = list(map(int,input().split()))
n,p,z=[],[],[]
z.append(0)
nc=0
pc=0
for i in range(num):
    if arr[i] < 0 :
        nc+=1
        n.append(arr[i])
    if arr [i] > 0:
        pc+=1
        p.append(arr[i])
if (nc %2==0):
    z.append(n[len(n)-1])
    n.remove(n[len(n)-1])

if (nc >=3):
    p.append(n[len(n)-1])
    p.append(n[len(n)-2])
    n.remove(n[len(n)-1])
    n.remove(n[len(n)-1])
n1,z1,p1="","",""    
print(len(n),n1.join([str(elem)+" " for elem in n]))        
print(len(p),p1.join([str(elem)+" " for elem in p]))
print(len(z),z1.join([str(elem)+" " for elem in z]))