num = list(map(int().split()))

even_num = num[1::2]
sum_val = sum(even_num)

third_num = num[2::3]
val = sum(third_num)/len(third_num)

print(sum_val,round(avg_val, 1))