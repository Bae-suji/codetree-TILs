num = input().split()
a = int(num[0])
b = int(num[1])

if a > b:
    for i in range(a,b-1,-1):
        print(f"{i}",end=" ")
else:
    for i in range(b,a-1,-1):
        print(f"{i}",end=" ")