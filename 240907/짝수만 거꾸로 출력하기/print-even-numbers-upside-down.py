n = int(input())

for i in range(n):
	
	arr = list(map(int, input().split()))

	arr[::-1]
    
	if arr[i] % 2 == 0:

		print(arr[i])