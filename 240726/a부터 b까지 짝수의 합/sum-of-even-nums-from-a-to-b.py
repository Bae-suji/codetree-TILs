num = input().split()
a = int(num[0])
b = int(num[1])
sum_val = 0

for i in range(a,b+1):
    if i % 2 == 0:
        sum_val += i
        
print(sum_val)