s = input()
i=0
c ="WUB"
n= len(s)
while i<n:
	if s[i:i+3] == c:
		i+=3
		print(end=" ")
	else:
		d =i
		i+=1
		print (s[d:i],end="")
