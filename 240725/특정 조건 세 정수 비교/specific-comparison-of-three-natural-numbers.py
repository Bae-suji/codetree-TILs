num = input().split()
a = int(num[0])
b = int(num[1])
c = int(num[2])

if a < b and a < c:
    d = 1
else:
    d = 0

if a == b == c:
    e = 1
else:
    e = 0
print(d,e)