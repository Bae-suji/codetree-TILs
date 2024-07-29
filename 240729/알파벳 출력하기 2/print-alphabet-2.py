n = int(input())
cnt = 'A'

for i in range(n):
    # 공백 출력
    for _ in range(i):
        print(" ", end=" ")
    
    # 알파벳 출력
    for _ in range(n - i):
        print(cnt, end=" ")
        cnt = chr(ord(cnt) + 1)
    
    print()