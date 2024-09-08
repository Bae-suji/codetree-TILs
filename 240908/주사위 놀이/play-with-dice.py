arr = list(map(int,input().split()))
arr_cnt = [0]*7

for elem in arr:
    arr_cnt[elem] += 1
    

for i in range(1,7):
    print(f"{i} - {arr_cnt[i]}")