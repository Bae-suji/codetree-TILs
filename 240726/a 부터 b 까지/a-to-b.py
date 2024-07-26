num = input().split()
a = int(num[0])
b = int(num[1])
i = a

while i <= b:
	print(i, end=" ")
	if i % 2 == 1:
		i *= 2
	else:
		i += 3