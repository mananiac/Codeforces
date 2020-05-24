for _ in range(int(input())):

	n,k = map(int,input().split())
	
	if n== k:
		print(1)
	else:
		for i in range(k,0,-1):
			if n%i==0:
				print(n//i)
				break

		# print(k)		