a, b = map(int,input().split())

arr = [0]*10
arr[0] = a
arr[1] = b

for i in range(2, 10): 
    arr[i] = (arr[i - 1] + arr[i - 2])%10
print(' '.join(map(str, arr)))