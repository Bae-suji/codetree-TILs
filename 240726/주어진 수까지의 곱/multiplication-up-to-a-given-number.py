num = input().split()
a = int(num[0])
b = int(num[1])

prod = 1

for i in range(a,b+1):
    prod *= i
print(prod)