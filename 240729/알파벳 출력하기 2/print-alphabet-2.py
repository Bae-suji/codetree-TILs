n = int(input())
cnt = 'A'

for i in range(1, n + 1):
    for _ in range(i - 1):
        print(" ", end=" ")
    

    for j in range(n - i + 1):
        print(cnt, end=" ")
        cnt = chr(ord(cnt) + 1)
    
    print()