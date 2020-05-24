for _ in range(int(input())):
	n,k = map(int,input().split())
	
	
	sum=n
	for i in range(k-1):
		
		num=list(map(int,str(n)))
		mini = min(num)
		maxi = max(num)
		sum = sum + mini*maxi
		n=sum
		# print(num,mini,maxi,sum)


	print (sum)
	# an+1=an+minDigit(an)⋅maxDigit(an).