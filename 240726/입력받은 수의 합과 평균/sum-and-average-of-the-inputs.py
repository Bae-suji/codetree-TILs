n = int(input())
sum_val = 0
ave_val = 0
cnt = 0

for i in range(n):
    i = int(input())
    sum_val += i
    cnt += 1

ave_val = sum_val/cnt
print(sum_val,"%0.1f"%ave_val)