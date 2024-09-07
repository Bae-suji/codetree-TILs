num = list(map(int,input().split()))

sum_even = sum(num[1::2])
sum_odd = sum(num[::2])

if sum_even > sum_odd:
    print(sum_even-sum_odd)
else:
    print(sum_odd-sum_even)