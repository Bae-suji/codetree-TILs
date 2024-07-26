num = input().split()
a = int(num[0])
b = int(num[1])
prod = 1

for i in range(1,b+1):
    if i % a == 0:
        prod *= i
print(prod)