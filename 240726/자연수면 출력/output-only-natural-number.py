num = input().split()
a = int(num[0])
b = int(num[1])

if a > 0:
    for i in range(b):
        print(f"{a}",end="")
else:
    print(0)