num = input().split()
sum_val = 0
ave_val = 0
cnt = 0

for elem in num:
	if int(elem) >= 250:
		break
	sum_val += int(elem)
	cnt += 1


ave_val = sum_val/cnt

print(sum_val, ave_val)