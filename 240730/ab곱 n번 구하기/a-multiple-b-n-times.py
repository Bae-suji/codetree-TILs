n = int(input())

for _ in range(n):
    arr = input().split()
    a = int(arr[0])
    b = int(arr[1])

    sum_val = 1
    for i in range(a, b + 1):
        sum_val *= i
    print(sum_val)