n = int(input())
cnt = 'A'

for i in range(n):
    for _ in range(i):
        print(" ", end=" ")
    
    for _ in range(n - i):
        print(cnt, end=" ")
        cnt = chr(ord(cnt) + 1)
    
    print()