

firstLine = list(input().split())

t = int(firstLine[0])
a = int(firstLine[1])
b = int(firstLine[2])

divisor = []
ans = []
for i in range(a,b+1):
    tempDivisor = [1]
    for j in range(2,i+1):
        if(i%j == 0):
            tempDivisor.append(j)
    divisor.append(set(tempDivisor))


for i in range(t):
    d = int(input())
    count = 0
    d_multiplier = d
    d_array = []
    j = 1
    while(b >= d_multiplier):
        d_array.append(d_multiplier)
        j = j + 1
        d_multiplier = d_multiplier * j
    d_set = set(d_array)
    d_num = 0
    for k in divisor:
        differense_set = k - d_set
        d_num = d_num + len(differense_set)
    ans.append(d_num)
for i in ans:
    print(i)
        
        
        
    




