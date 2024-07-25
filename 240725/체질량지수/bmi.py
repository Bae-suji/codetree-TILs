inp = input().split()
h = int(inp[0])
w = int(inp[1])

a = (10000*w)//(h*h)
print(a)
if a >= 25:
    print("Obesity")