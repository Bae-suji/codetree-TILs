num = input().split()
a = int(num[0])
b = int(num[1])

if a > b:
    print(f"{a*b}")
else:
    print(f"{b//a}")