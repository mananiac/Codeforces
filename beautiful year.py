year=int(input())
a=""
for i in range(year+1,9013):
    i=list(str(i))
    if (i[0] == i[1] or i[0]==i[2]or i[0] ==i[3] or i[1] ==i[2] or i[1] ==i[3] or i[2] == i[3] ):
        continue
    else:
        for j in i:
            a=a+j
        print(a)
        break
