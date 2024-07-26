sum_val = 0
ave_val = 0
cnt = 0

while True:
    n = int(input())
    
    if n >= 30:
        break

    sum_val += n
    cnt += 1
    ave_val = sum_val/cnt   
    
print(f"%0.2f"%ave_val)