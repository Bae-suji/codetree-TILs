num = input().split()
a = int(num[0])
b = int(num[1])
c = int(num[2])

if a <= b <= c:
    print(b)
elif c <= b <= a:
    print(b)
elif a <= c <= b:
    print(c)
elif b <= c <= a:
    print(c)
elif b <= a <= c:
    print(a)
elif c <= a <= b:
    print(a)