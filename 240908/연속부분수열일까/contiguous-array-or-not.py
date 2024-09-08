n1, n2 = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 연속 부분 수열 확인
found = False
for i in range(n1 - n2 + 1):  # A에서 B의 길이만큼의 구간을 확인
    if A[i:i + n2] == B:
        found = True
        break

# 결과 출력
if found:
    print("Yes")
else:
    print("No")