# 1 이상 10 이하의 정수를 입력받습니다.
n = int(input())

# 결과를 저장할 배열
arr = []

# 5의 배수가 출력된 횟수를 세는 변수
count_five_multiples = 0

# i는 1부터 시작하여 계속 증가시키면서 n의 배수를 구합니다.
i = 1
while count_five_multiples < 2:
    multiple = n * i
    arr.append(multiple)
    
    # 5의 배수인 경우 count_five_multiples를 증가시킵니다.
    if multiple % 5 == 0:
        count_five_multiples += 1

    # 두 번째 5의 배수가 나오면 루프 종료
    if count_five_multiples == 2:
        break
    
    i += 1

# 결과를 공백으로 구분하여 출력합니다.
print(' '.join(map(str, arr)))