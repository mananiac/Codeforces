for _ in range(int(input())):
	num=int(input())
	arr = list(map(int,input().split()))
	count=0
	for i in arr:
		if i==1:
			count+=1
	m=max(arr)
	if count==num:
		print(count)
	elif m==num:
		print(1)
	# eif m>num:

	else:		
		num=num-count
		print(count+num//m)
	