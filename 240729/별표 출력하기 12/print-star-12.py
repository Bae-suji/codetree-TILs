n = int(input())
	
for i in range(n):
	if i == 0:
		print("*", end=" ")

for j in range(n):
		if j % 2 != 0:
			print("*", end=" ")
		else:
			print("",end=" ")