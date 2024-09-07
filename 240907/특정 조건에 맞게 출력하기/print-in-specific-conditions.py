n = list(map(int,input().split()))
arr = []

for i in n:
    if i == 0:
        break
    if i % 2 == 1:
        i += 3
        arr.append(i)
    else:
        i //= 2
        arr.append(i)

print(' '.join(map(str, arr)))