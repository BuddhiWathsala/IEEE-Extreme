

def fib(n, computed = {0: 0, 1: 1}):
      
    if n not in computed:
        computed[n] = fib(n-1, computed) + fib(n-2, computed)
    return computed[n]

t = int(input())
ans = []
for i in range(t):
    m = int(input())
    f = int(fib(m+1))
    num = f%10
    ans.append(num)
for i in ans:
    print(i)
    
