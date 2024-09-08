n = int(input())
arr = [0]*100
arr[0] = 1
arr[1] = n

i = 2
while True:
    arr[i] = arr[i - 1] + arr[i - 2]
    if arr[i] > 100:
        break
    i += 1

arr[i] = arr[i - 1] + arr[i - 2]

print(' '.join(map(str, arr[:i+1])))