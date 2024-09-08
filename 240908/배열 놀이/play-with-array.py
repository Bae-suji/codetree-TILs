n, q = map(int,input().split())
arr = list(map(int, input().split()))

for _ in range(q):
    query = input().split()
    
    if query[0] == '1':  # 첫 번째 질의 "1 a"
        a = int(query[1])
        print(arr[a - 1])  # 배열은 0-indexed이므로 a-1번째 원소를 출력
    
    elif query[0] == '2':  # 두 번째 질의 "2 b"
        b = int(query[1])
        if b in arr:
            print(arr.index(b) + 1)  # 0-indexed이므로 +1을 해서 출력
        else:
            print(0)  # 값이 없을 경우 0 출력
    
    elif query[0] == '3':  # 세 번째 질의 "3 s e"
        s, e = int(query[1]), int(query[2])
        print(' '.join(map(str, arr[s - 1:e])))  # s번째부터 e번째까지 출력 (1-indexed이므로 -1)