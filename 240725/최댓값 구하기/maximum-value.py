num = input().split()
a = int(num[0])
b = int(num[1])
c = int(num[2])

if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
elif c >= b and c >= a:
    print(c)