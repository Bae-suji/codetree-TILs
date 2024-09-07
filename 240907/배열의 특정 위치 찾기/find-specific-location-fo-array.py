num = list(map(int, input().split()))

# 짝수 번째로 입력된 값의 합과 3의 배수 번째로 입력된 값의 합, 평균을 구하는 변수
even_sum = 0
third_sum = 0
third_count = 0

# 인덱스는 0부터 시작하므로 짝수 번째 값은 인덱스가 홀수(1, 3, 5, ...)인 값들이 해당됩니다.
for i in range(10):
    if (i + 1) % 2 == 0:  # 짝수 번째 값 (인덱스는 1, 3, 5, ...)
        even_sum += num[i]
    if (i + 1) % 3 == 0:  # 3의 배수 번째 값 (인덱스는 2, 5, 8)
        third_sum += num[i]
        third_count += 1

# 3의 배수 번째 값의 평균을 구합니다.
third_avg = third_sum / third_count if third_count > 0 else 0

# 결과를 출력합니다.
print(even_sum, round(third_avg, 1))