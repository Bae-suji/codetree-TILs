inp = input().split()
c = inp[0]
n = int(inp[1])

if c == 'A':
    for i in range(1,n+1):
        print(f"{i}",end=" ")
else:
    for i in range(n,0):
        print(f"{i}",end=" ")