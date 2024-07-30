num = input().split()
start = int(num[0])
end = int(num[1])
val2 = 0


for i in range(start,end+1):
    sum_val = 0
    for j in range(1,i+1):
        if i % j == 0:
            sum_val += 1
        
    if sum_val == 3:
        val2 += 1
    
print(val2)