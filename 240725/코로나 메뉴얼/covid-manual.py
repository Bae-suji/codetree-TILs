a = input().split()
b = input().split()
c = input().split()

a1 = a[0]
a2 = int(a[1])
b1 = b[0]
b2 = int(b[1])
c1 = c[0]
c2 = int(c[1])

if a1 == "Y" and b1 == "Y":
    if a2 >= 37 and  b2 >= 37:
        print("E")
    else:
        print("N")

if a1 == "Y" and c1 == "Y":
    if a2 >= 37 and c2 >= 37:
        print("E")
    else:
        print("N")

if b1 == "Y" and c1 == "Y":
    if b2 >= 37 and c2 >= 37:
        print("E")
    else:
        print("N")