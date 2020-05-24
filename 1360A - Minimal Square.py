for _ in range(int(input())):

	a,b = map(int,input().split())

	area = 2*a*b
	if a>=b:
		big=a
		small=b
	else:
		big= b
		small = a
	print(max(2*small,big)**2)