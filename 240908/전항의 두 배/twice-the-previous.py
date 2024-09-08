a1, a2 = list(map(int, input().split()))
arr = [a1, a2]

for i in range(2,10):
    next_value = arr[i - 1] + 2*arr[i - 2]
    arr.append(next_value)
    
print(' '.join(map(str, arr)))