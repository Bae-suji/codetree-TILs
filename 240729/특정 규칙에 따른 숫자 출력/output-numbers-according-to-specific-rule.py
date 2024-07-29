n = int(input())
cnt = 0

for i in range(1, n+1):
    for j in range(1, n+1):
        if j < i:
            print(" ", end=" ")
        else:
            cnt += 1
            if cnt > 9:
                cnt = 1
            print(cnt, end=" ")
    print()