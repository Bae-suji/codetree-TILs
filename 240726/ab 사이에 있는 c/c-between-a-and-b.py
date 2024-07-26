num = input().split()
a = int(num[0])
b = int(num[1])
c = int(num[2])
result = 'NO'

for i in range(a,b+1):

    if i % c == 0:
        result ='YES'

print(result)