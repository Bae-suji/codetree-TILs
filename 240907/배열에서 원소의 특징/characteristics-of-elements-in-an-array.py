num = list(map(int,input().split()))
result = 0
for i in range(len(num)):
    if num[i] % 3 == 0:
        result = i
        break

print(num[i-1])