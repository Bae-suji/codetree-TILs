sum_val,ave_val,cnt = 0,0,0

while True:
    n = int(input())
    
    if n >= 30:
        break

    sum_val += n
    cnt += 1
    ave_val = sum_val/cnt   

print(f"%0.2f"%ave_val)