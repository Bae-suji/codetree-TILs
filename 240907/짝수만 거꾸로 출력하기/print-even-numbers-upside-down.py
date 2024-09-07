n = int(input())

# n개의 정수를 리스트로 입력
arr = list(map(int, input().split()))

even_numbers = []

# 리스트를 순회하면서 짝수만 even_numbers에 추가합니다.
for num in arr:
    if num % 2 == 0:
        even_numbers.append(num)

# 짝수 리스트를 역순으로 출력합니다.
print(' '.join(map(str, reversed(even_numbers))))