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
    # 첫 번째 사람이 A라면, 남은 두 사람 중 한 사람이라도 A면 됩니다.
    if (c2 == 'Y' and t2 >= 37) or (c3 == 'Y' and t3 >= 37):
        print("E")
    else:
        print("N")
else:
    # 첫 번째 사람이 A가 아니라면, 남은 두 사람 모두 A여야만 합니다.
    if (c2 == 'Y' and t2 >= 37) and (c3 == 'Y' and t3 >= 37):
        print("E")
    else:
        print("N")