inp = input().split()
a = int(inp[0])
b = int(inp[1])

if a > b:
    print(f"{a-b}")
else:
    print(f"{b-a}")