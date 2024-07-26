num = input().split()
a = int(num[0])
b = int(num[1])
result = 0
for i in range(a,b+1):
    if 1920 % i == 0 and 2880 % i == 0:
        result = 1
print(result)