num = input().split()
a = int(num[0])
b = int(num[1])
c = a/b

print(f"{a//b}.", end="")
a %= b
for _ in range(20):
    a *= 10
    print(a // b, end="")
    a %= b