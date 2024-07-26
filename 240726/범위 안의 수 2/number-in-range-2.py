sum_val = 0
ave_val = 0
cnt = 0

for i in range(10):
    i = int(input())
    if 0 <= i <= 200:
        sum_val += i
        cnt += 1

ave_val = sum_val/cnt
print(sum_val,f"%0.1f"%ave_val)