n = int(input())
num = 0

for i in range(1,20):
    n //= i
    num += 1
    if n <= 1:
        break
        
print(num)