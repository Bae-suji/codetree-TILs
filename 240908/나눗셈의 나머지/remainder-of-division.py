a, b = map(int, input().split())

remainder_count = {}

while a > 1:
    remainder = a % b
    if remainder in remainder_count:
        remainder_count[remainder] += 1
    else:
        remainder_count[remainder] = 1
    a //= b

# 나머지의 등장 횟수 제곱의 합을 계산합니다.
sum_of_squares = sum(count ** 2 for count in remainder_count.values())

# 결과를 출력합니다.
print(sum_of_squares)