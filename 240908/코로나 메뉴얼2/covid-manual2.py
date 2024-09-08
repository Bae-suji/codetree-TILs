# 각 진료소를 위한 카운트를 초기화합니다.
count_A = 0
count_B = 0
count_C = 0
count_D = 0

# 위급상황을 체크할 카운트 변수
urgent_count = 0

# 입력을 받아서 처리합니다.
for _ in range(3):
    symptoms, temperature = input().split()
    temperature = int(temperature)
    
    if symptoms == 'Y':
        if temperature >= 37:
            count_A += 1
        else:
            count_C += 1
    else:
        if temperature >= 37:
            count_B += 1
        else:
            count_D += 1

# 위급상황 여부를 판단합니다.
if count_A >= 2:
    urgent_status = 'E'
else:
    urgent_status = ''

# 결과를 출력합니다.
print(count_A, count_B, count_C, count_D, urgent_status)