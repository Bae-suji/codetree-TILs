num = int(input())
score = list(map(float, input().split()))

sum_val = sum(score)
ave = sum_val/num

print(f"{ave:.1f}")

if ave >= 4.0:
    print("Perfect")
elif ave >= 3.0:
    print("Good")
else:
    print("Poor")