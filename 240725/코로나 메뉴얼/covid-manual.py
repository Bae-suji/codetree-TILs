a = input().split()
b = input().split()
c = input().split()

a1 = a[0]
a2 = int(a[1])
b1 = b[0]
b2 = int(b[1])
c1 = c[0]
c2 = int(c[1])

if c1 == 'Y' and t1 >= 37:
    if (c2 == 'Y' and t2 >= 37) or (c3 == 'Y' and t3 >= 37):
        print("E")
    else:
        print("N")
else:
    if (c2 == 'Y' and t2 >= 37) and (c3 == 'Y' and t3 >= 37):
        print("E")
    else:
        print("N")