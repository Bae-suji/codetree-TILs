n = int(input())
num = map(int,input().split())

arr = [i for i in num if i % 2 == 0]
print(' '.join(map(str,arr)))