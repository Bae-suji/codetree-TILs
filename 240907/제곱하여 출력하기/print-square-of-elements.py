n = int(input())
num = list(map(int, input().split()))

arr = [i*i for i in num]
print(' '.join(map(str,arr)))