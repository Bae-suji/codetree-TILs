n = int(input())

# n개의 정수를 리스트로 입력
arr = list(map(int, input().split()))

for num in reversed(arr):
	
	if num % 2 == 0:

		print(num)