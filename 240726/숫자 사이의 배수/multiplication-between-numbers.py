num = input().split()
a = int(num[0])
b = int(num[1])
sum_val = 0
ave_val = 0
cnt = 0

for i in range(a,b+1):
    if i % 5 == 0 or i % 7 == 0:
        sum_val += i
        cnt += 1

ave_val = sum_val/cnt      
print(sum_val, f"%0.1f"%ave_val)