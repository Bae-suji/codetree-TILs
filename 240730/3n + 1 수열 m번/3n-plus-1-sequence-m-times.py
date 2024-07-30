m = int(input())

for _ in range(m):
    n = int(input())
    sum_val = 0

    while n != 1:
        if n % 2 == 0:
            n //= 2
            
        else: 
            n = n * 3 + 1 

        sum_val += 1
             
    print(sum_val)