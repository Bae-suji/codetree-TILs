n = list(map(int,input().split()))
arr_cnt = [0]*11

for elem in n:
    if elem == 0:
        break
    if elem >= 10:
        score = elem // 10
        arr_cnt[score] += 1

for i in range(100,9,-10):
    print(f"{i} - {arr_cnt[i//10]}")