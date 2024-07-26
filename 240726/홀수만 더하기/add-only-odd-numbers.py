n = int(input())
sum_val = 0

for i in range(n):
    i = int(input())
    if i % 2 != 0 and i % 3 == 0:
        sum_val += 1 
print(sum_val)