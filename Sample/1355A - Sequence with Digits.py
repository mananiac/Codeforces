
a=int(input())
for j in range(a):
	n,k = map(int,input().split())
	
	
	sum=n
	num=n
	maxi=0
	mini=n%10
	for i in range(k-1):
		while(num>0):
			r=num%10
			num=num//10
			if (r>=maxi):
				maxi=r
			elif(r<mini):
				mini=r

		# num=list(map(int,str(n)))
		# mini = min(num)
		# maxi = max(num)
		sum = sum + mini*maxi
		# n=sum
		
		# print(num,mini,maxi,sum)
		num=sum
		maxi=0
		mini=sum%10


	print (sum)
	# an+1=an+minDigit(an)⋅maxDigit(an).