t = int(input())

def NCR(n,c):
    ans = 1
    nc = n-c
    for i in range(1,c+1):
        ans = ans * (nc+ i)
        ans = ans / i
    
    return int(ans)

for i in range(t):
    line = list(input().split(" "))
    a = int(line[0])
    b = int(line[1])
    c = int(line[2])
    ncr = 0
    if(a == 0):
        print(0)
        continue
    elif(a == 1):
        print(1)
        continue
    elif((b != c) and ((b/2) < c)):
        ncr = NCR(b,(b-c))
    else:
        ncr = NCR(b,c)
    
    answer = pow(a,ncr)
    md = pow(10,9) + 7
    print(answer%md)
