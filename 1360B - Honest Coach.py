for _ in range(int(input())):
	n=int(input())
	arr = list(map(int,input().split()))
	mini=arr[1]-arr[0]
	for i in range(0,n):
		for j in range(i+1,n):
			mini = abs(min(abs(arr[i] - arr[j]) , mini))

	print(abs(mini))
