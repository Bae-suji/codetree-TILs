n = int(input())
arr = [0]*100
arr[0] = 1
arr[1] = n

                 
for i in range(2, 10):
    if arr[i] <= 100: 
        arr[i] = (arr[i - 1] + arr[i - 2])
    else:
        break

print(' '.join(map(str, arr[:i])))