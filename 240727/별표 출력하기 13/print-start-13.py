# 사용자로부터 정수 n 입력받기
n = int(input())

# 총 출력해야 할 줄의 개수는 2 * n 입니다
for i in range(1, (2 * n) + 1):
    # 홀수번째 줄인 경우 n - (i // 2) 개의 별을 출력
    if i % 2 == 1:
        count = n - (i // 2)
    # 짝수번째 줄인 경우 i // 2 개의 별을 출력
    else:
        count = i // 2

    # count 개수만큼 별 출력
    for _ in range(count):
        print("*", end=" ")
    # 줄바꿈
    print()